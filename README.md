# ChargeGrid Intelligence - Prova de Conceito

Projeto desenvolvido para a Sprint 2 da disciplina **Pensamento Computacional e Automação com Python**, dentro do **GoodWe Challenge**.

## Sobre o Projeto

O **ChargeGrid Intelligence** é uma prova de conceito funcional que simula o gerenciamento inteligente de recarga de veículos elétricos.

A proposta evolui a ideia apresentada na Sprint 1, transformando o conceito em uma aplicação prática com interface visual, controle de demanda, tarifação dinâmica e simulação de decisões inteligentes.

## Objetivo

Demonstrar, de forma simples e funcional, como um sistema pode auxiliar no controle de pontos de recarga para veículos elétricos, considerando:

- quantidade de veículos conectados;
- limite de capacidade da rede elétrica;
- horário de pico;
- variação no custo da energia;
- distribuição da potência entre os veículos;
- comunicação simulada com os carregadores.

## Funcionalidades

- Simulação de veículos elétricos conectados;
- Definição da capacidade máxima da rede em kW;
- Identificação de horário de pico;
- Tarifação dinâmica por kWh;
- Controle automático da potência por veículo;
- Simulação de decisão inteligente pelo "ChargeGrid Brain";
- Exibição de status dos pontos de recarga;
- Logs simulados de interoperabilidade utilizando protocolo OCPP.

## Tecnologias Utilizadas

- Python
- Streamlit

## Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/C0utinhoxx/Sp2Py.git
```

2. Acesse a pasta do projeto:

```bash
cd Sp2Py
```

3. Instale as dependências:

```bash
python3 -m pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python3 -m streamlit run app.py
```

Após executar o comando, o sistema será aberto no navegador.

## Lógica da Solução

O sistema considera que cada veículo elétrico pode consumir até **11 kW** durante a recarga.

A demanda máxima teórica é calculada pela fórmula:

```text
Demanda máxima = quantidade de veículos conectados x 11 kW
```

Caso a demanda ultrapasse o limite da rede, ou o sistema esteja em horário de pico, o **ChargeGrid Brain** ativa uma restrição e redistribui a potência disponível entre os veículos.

Quando não há risco de sobrecarga, o sistema mantém a operação normal, liberando a potência máxima para os veículos.

## Tarifação

A aplicação simula dois cenários de tarifa:

- Horário de pico: tarifa mais cara;
- Horário fora de pico: tarifa mais barata.

Essa lógica representa a variação do custo da energia conforme o período do dia.

## Interoperabilidade

A prova de conceito também apresenta logs simulados do protocolo **OCPP**, representando a comunicação entre os pontos de recarga e o sistema de gerenciamento.

Exemplos de mensagens simuladas:

```text
BootNotification.req
SetChargingProfile.req
Heartbeat.req
```

## Evolução em Relação à Sprint 1

Na Sprint 1, a equipe apresentou a proposta conceitual do ChargeGrid Smart Manager, explicando o problema, a solução e os principais recursos planejados.

Na Sprint 2, a proposta evoluiu para uma prova de conceito funcional, permitindo visualizar na prática:

- controle de demanda;
- simulação de recarga;
- tomada de decisão automática;
- tarifação dinâmica;
- comunicação entre sistema e carregadores.

## Estrutura do Projeto

```text
Sp2Py/
├── app.py
├── README.md
└── requirements.txt
```

## Integrantes

- Lucas Lino Marques da Silva - RM 572863
- Bruno Riquelme Coutinho Pereira - RM 569619
- Eduardo Bigoli Portela - RM 569897
- Gabriel Martins Cordeiro Rodrigues - RM 570497
- Gustavo Fondato de Souza - RM 573651
- Gustavo Martins da Silva - RM 570584

## Observação

Este projeto é uma simulação acadêmica desenvolvida para demonstrar a lógica de funcionamento da solução proposta. A integração OCPP e o motor de IA são representados de forma simplificada para fins de prova de conceito.