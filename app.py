import streamlit as st
import datetime
import random

st.set_page_config(page_title="ChargeGrid Intelligence - PoC", layout="wide")

st.title("ChargeGrid Intelligence - Prova de Conceito")
st.subheader("GoodWe Challenge - Gerenciamento Inteligente de Recarga")
st.markdown("---")

st.sidebar.header("Parametros da Rede e Simulacao")

hora_simulada = st.sidebar.slider("Horario da Simulacao (Hora do Dia)", 0, 23, 19)
veiculos_conectados = st.sidebar.number_input("Veiculos Eletricos Conectados", min_value=1, max_value=20, value=5)
limite_transformador = st.sidebar.slider("Capacidade Maxima da Rede (kW)", 20, 150, 50)

if 18 <= hora_simulada <= 21:
    tipo_tarifa = "Horario de Pico (Mais Cara)"
    custo_kwh = 1.20
    status_rede = "Critico / Sobrecarga"
else:
    tipo_tarifa = "Horario Fora de Pico (Mais Barata)"
    custo_kwh = 0.45
    status_rede = "Estavel / Normal"

demanda_maxima_teorica = veiculos_conectados * 11

if demanda_maxima_teorica > limite_transformador or status_rede == "Critico / Sobrecarga":
    potencia_permitida_por_veiculo = round(limite_transformador / veiculos_conectados, 2)
    potencia_permitida_por_veiculo = max(2.2, potencia_permitida_por_veiculo)
    acao_ia = "Restricao Ativada: Potencia racionada igualmente entre os veiculos."
else:
    potencia_permitida_por_veiculo = 11.0
    acao_ia = "Operacao Normal: Potencia maxima liberada para todos os veiculos."

potencia_total_atual = potencia_permitida_por_veiculo * veiculos_conectados

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Status da Rede Eletrica", value=status_rede)
with col2:
    st.metric(label="Tarifa Atual (R$ / kWh)", value=f"R$ {custo_kwh:.2f}", delta=tipo_tarifa, delta_color="inverse" if "Pico" in tipo_tarifa else "normal")
with col3:
    st.metric(label="Potencia Permitida por Carro", value=f"{potencia_permitida_por_veiculo} kW")
with col4:
    st.metric(label="Carga Total no Hub", value=f"{potencia_total_atual:.1f} kW", delta=f"Limite: {limite_transformador} kW", delta_color="inverse" if potencia_total_atual > limite_transformador else "normal")

st.markdown("---")

st.subheader("Decisao do Motor de IA (ChargeGrid Brain)")
if "Restricao" in acao_ia:
    st.warning(f"Analise da IA: {acao_ia}")
else:
    st.success(f"Analise da IA: {acao_ia}")

st.subheader("Status dos Pontos de Recarga (Interoperabilidade OCPP)")

col_v1, col_v2 = st.columns([2, 1])

with col_v1:
    st.write("Dispositivos gerenciados em tempo real pelo ChargeGrid:")
    for i in range(1, veiculos_conectados + 1):
        soc_atual = random.randint(20, 85)
        st.text(f"Vaga 0{i} - EV ID: 000{i*12} | Status: Carregando | SoC: {soc_atual}% | Potencia Recebida: {potencia_permitida_por_veiculo} kW")

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