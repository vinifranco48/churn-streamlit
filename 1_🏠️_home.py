import streamlit as st
import webbrowser
import pandas as pd


if 'data' not in st.session_state:
    df_data = pd.read_csv('dataset/train.csv')
    st.session_state['data'] = df_data
df_data = st.session_state['data']
st.markdown('''
            # Analise de churn
            ''')
st.sidebar.markdown('Desenvolvido por [Vinicius](https://www.linkedin.com/in/vinicius-franco-720558228/)')
btn = st.button("Acesse os dados utilizados")

if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/competitions/playground-series-s4e1')


st.markdown('''### Dados de Clientes de um Banco

Os dados fornecidos representam informações sobre clientes de um banco. Abaixo está uma explicação detalhada de cada coluna:

- **id**: Identificador único para cada cliente.
- **CustomerId**: Número de identificação do cliente.
- **Surname**: Sobrenome do cliente.
- **CreditScore**: Pontuação de crédito atribuída ao cliente.
- **Geography**: País onde o cliente reside.
- **Gender**: Gênero do cliente.
- **Age**: Idade do cliente.
- **Tenure**: Tempo de permanência (em anos) do cliente no banco.
- **Balance**: Saldo da conta do cliente.
- **NumOfProducts**: Número de produtos bancários que o cliente utiliza.
- **HasCrCard**: Indica se o cliente possui cartão de crédito (1 para sim, 0 para não).
- **IsActiveMember**: Indica se o cliente é um membro ativo (1 para sim, 0 para não).
- **EstimatedSalary**: Salário estimado do cliente.
- **Exited**: Indica se o cliente encerrou o relacionamento com o banco (1 para sim, 0 para não).

Esses dados podem ser utilizados para análises estatísticas, modelagem preditiva e outras tarefas relacionadas à gestão de clientes em instituições financeiras.''' )

df_data