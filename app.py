import streamlit as st
import datetime
import random

st.set_page_config(page_title="ChargeGrid Intelligence - PoC", layout="wide")

st.title("ChargeGrid Intelligence - Prova de Conceito")
st.subheader("GoodWe Challenge - Gerenciamento Inteligente de Recarga")
st.markdown("---")

st.sidebar.header("Parâmetros da Rede e Simulação")

hora_simulada = st.sidebar.slider("Horário da Simulação (Hora do Dia)", 0, 23, 19)
veiculos_conectados = st.sidebar.number_input("Veículos Elétricos Conectados", min_value=1, max_value=20, value=5)
limite_transformador = st.sidebar.slider("Capacidade Máxima da Rede (kW)", 20, 150, 50)

if 18 <= hora_simulada <= 21:
    tipo_tarifa = "Horário de Pico (Mais Cara)"
    custo_kwh = 1.20
    status_rede = "Crítico / Sobrecarga"
else:
    tipo_tarifa = "Horário Fora de Pico (Mais Barata)"
    custo_kwh = 0.45
    status_rede = "Estável / Normal"

demanda_maxima_teorica = veiculos_conectados * 11

if demanda_maxima_teorica > limite_transformador or status_rede == "Crítico / Sobrecarga":
    potencia_permitida_por_veiculo = round(limite_transformador / veiculos_conectados, 2)
    potencia_permitida_por_veiculo = max(2.2, potencia_permitida_por_veiculo)
    acao_ia = "Restrição Ativada: Potência racionada igualmente entre os veículos."
else:
    potencia_permitida_por_veiculo = 11.0
    acao_ia = "Operação Normal: Potência máxima liberada para todos os veículos."

potencia_total_atual = potencia_permitida_por_veiculo * veiculos_conectados

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Status da Rede Elétrica", value=status_rede)
with col2:
    st.metric(label="Tarifa Atual (R$ / kWh)", value=f"R$ {custo_kwh:.2f}", delta=tipo_tarifa, delta_color="inverse" if "Pico" in tipo_tarifa else "normal")
with col3:
    st.metric(label="Potência Permitida por Carro", value=f"{potencia_permitida_por_veiculo} kW")
with col4:
    st.metric(label="Carga Total no Hub", value=f"{potencia_total_atual:.1f} kW", delta=f"Limite: {limite_transformador} kW", delta_color="inverse" if potencia_total_atual > limite_transformador else "normal")

st.markdown("---")

st.subheader("Decisão do Motor de IA (ChargeGrid Brain)")
if "Restrição" in acao_ia:
    st.warning(f"Análise da IA: {acao_ia}")
else:
    st.success(f"Análise da IA: {acao_ia}")

st.subheader("Status dos Pontos de Recarga (Interoperabilidade OCPP)")

col_v1, col_v2 = st.columns([2, 1])

with col_v1:
    st.write("Dispositivos gerenciados em tempo real pelo ChargeGrid:")
    for i in range(1, veiculos_conectados + 1):
        soc_atual = random.randint(20, 85)
        st.text(f"Vaga 0{i} - EV ID: 000{i*12} | Status: Carregando | SoC: {soc_atual}% | Potência Recebida: {potencia_permitida_por_veiculo} kW")

with col_v2:
    st.write("Logs de Interoperabilidade (Protocolo OCPP):")
    st.code(
        f"[{datetime.datetime.now().strftime('%H:%M:%S')}] BootNotification.req -> Aceito\n"
        f"[{datetime.datetime.now().strftime('%H:%M:%S')}] SetChargingProfile.req ({potencia_permitida_por_veiculo} kW)\n"
        f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Heartbeat.req -> OK",
        language="json"
    )

st.markdown("---")
st.caption("ChargeGrid Intelligence Prova de Conceito v2.0 - Desenvolvido para a FIAP / GoodWe Challenge 2026.")