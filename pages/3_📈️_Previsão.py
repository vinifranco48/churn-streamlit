import streamlit as st
import pandas as pd
import joblib

# Definindo as cores personalizadas
COR_PRINCIPAL = '#1E90FF'
COR_SECUNDARIA = '#D3D3D3'

# Configuração da página
st.set_page_config(
    page_title="Previsão de Churn",
    layout="wide",
    page_icon="📊"
)

# Título do aplicativo
st.title('Previsão de Churn')

# Adicionar seção para entrada do usuário
st.sidebar.header('Entradas do Usuário')

# Adicionar controles para entrada do usuário
credit_score = st.sidebar.number_input('Credit Score', min_value=300, max_value=850, value=650)
geography = st.sidebar.selectbox('Geography', ['France', 'Spain', 'Germany'])
gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
age = st.sidebar.number_input('Age', min_value=18, max_value=100, value=30)
tenure = st.sidebar.number_input('Tenure', min_value=0, max_value=10, value=5)
balance = st.sidebar.number_input('Balance', min_value=0.0, max_value=250000.0, value=50000.0)
num_of_products = st.sidebar.number_input('Num Of Products', min_value=1, max_value=4, value=2)
has_cr_card = st.sidebar.selectbox('Has Credit Card', ['No', 'Yes'])
is_active_member = st.sidebar.selectbox('Is Active Member', ['No', 'Yes'])
estimated_salary = st.sidebar.number_input('Estimated Salary', min_value=0.0, max_value=200000.0, value=100000.0)

# Mapear as colunas categóricas para valores numéricos
geography_map = {'France': 0, 'Spain': 1, 'Germany': 2}
gender_map = {'Male': 0, 'Female': 1}
yes_no_map = {'No': 0, 'Yes': 1}

# Armazenar entrada do usuário em um DataFrame
user_input = pd.DataFrame({
    'CreditScore': [credit_score],
    'Geography': [geography_map[geography]],
    'Gender': [gender_map[gender]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [yes_no_map[has_cr_card]],
    'IsActiveMember': [yes_no_map[is_active_member]],
    'EstimatedSalary': [estimated_salary]
})

# Carregar o modelo serializado
model = joblib.load('notebooks/modelo_treinado.joblib')

# Prever usando o modelo
prediction = model.predict(user_input)

# Exibir a previsão
st.subheader('Previsão:')
if prediction[0] == 1:
    st.write('O cliente provavelmente fará churn.')
else:
    st.write('O cliente provavelmente não fará churn.')

# Estilizando o sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: %s;
    }
    </style>
    """
    % COR_SECUNDARIA,
    unsafe_allow_html=True
)
