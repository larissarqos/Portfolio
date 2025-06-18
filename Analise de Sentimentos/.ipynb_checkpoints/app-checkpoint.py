import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import re

# - Pré-processamento de texto
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords_pt = set(stopwords.words('portuguese'))

def limpar_texto(texto):
    texto = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', str(texto))
    texto = texto.lower()
    palavras = texto.split()
    palavras = [p for p in palavras if p not in stopwords_pt]
    return ' '.join(palavras)

# -- Carregamento do modelo e vetor
modelo = joblib.load('modelo_logistico.pkl')
vetor = joblib.load('vetor_countvectorizer.pkl')

# -- Sidebar
st.sidebar.title("Menu")
opcao = st.sidebar.radio("Escolha uma opção:", ["Gerar Nuvem de Palavras", "Analisar Avaliação"])

# -- Título e descrição do app
st.markdown("<h1 style='text-align: center;'>💬 Análise de Sentimentos</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><i>App de análise de sentimentos em avaliações de produtos</i></p>", unsafe_allow_html=True)
st.divider()

# -- Opção: Ver nuvens de palavras
if opcao == "Gerar Nuvem de Palavras":
    st.markdown("Faça o upload de um arquivo .csv com avaliações para gerar a nuvem de palavras")
    arquivo = st.file_uploader("Fazer upload do arquivo CSV", type=["csv"])

    if arquivo is not None:
        try:
            df = pd.read_csv(arquivo, encoding='utf-8', on_bad_lines='skip')
        except Exception as e:
            st.error(f"Erro ao ler o arquivo CSV: {e}")
            st.stop()

        st.write("Prévia dos dados:")
        st.dataframe(df.head())

        df = df.dropna(subset=['review_comment_message'])
        df['texto_limpo'] = df['review_comment_message'].apply(limpar_texto)

        if st.button("Gerar Nuvem de Palavras"):
            from sklearn.feature_extraction.text import CountVectorizer

            stopwords_pt_lista = list(stopwords_pt)

            def gerar_ngrams(textos, n=3):
                vectorizer = CountVectorizer(ngram_range=(1, n), stop_words=stopwords_pt_lista)
                X = vectorizer.fit_transform(textos)
                soma = X.sum(axis=0)
                frequencias = {palavra: soma[0, idx] for palavra, idx in vectorizer.vocabulary_.items()}
                return frequencias

            frequencias = gerar_ngrams(df['texto_limpo'], n=3)

            st.divider()
            st.markdown("<h3 style='text-align: center;'>Nuvem de Palavras das Avaliações</h3>", unsafe_allow_html=True)
            wordcloud = WordCloud(width=1200, height=800, background_color='black').generate_from_frequencies(frequencias)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)


# -- Opção: Analisar Avaliação
elif opcao == "Analisar Avaliação":
    st.markdown("<h4>Digite uma avaliação para análise</h4>", unsafe_allow_html=True)
    frase = st.text_input("", placeholder="Exemplo: Gostei muito do produto, chegou rápido e bem embalado")
    
    st.markdown("")
    
    if st.button("Analisar") and frase:
        frase_limpa = limpar_texto(frase)
        frase_vetor = vetor.transform([frase_limpa])
        predicao = modelo.predict(frase_vetor)[0]
        if predicao == 1:
            sentimento = "Avaliação Positiva 😊"
            st.success(sentimento)
        else:
            sentimento = "Avaliação Negativa 😞"
            st.error(sentimento)
        