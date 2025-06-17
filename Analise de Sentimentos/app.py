import streamlit as st
import joblib

# Carrega o modelo e o vetor
modelo = joblib.load('modelo_logistico.pkl')
vetor = joblib.load('vetor_countvectorizer.pkl')

# Interface do app
st.title("Analisador de Sentimentos")

frase = st.text_input("Digite uma frase para análise:")

if frase:
    frase_vetor = vetor.transform([frase])
    predicao = modelo.predict(frase_vetor)[0]
    sentimento = "Positivo 😊" if predicao == 1 else "Negativo 😞"
    st.write(f"**Resultado:** {sentimento}")