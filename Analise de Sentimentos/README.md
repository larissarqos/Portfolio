<h1 align="center">Análise de Satisfação de Clientes de E-commerce</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/5f0649ed-982e-4bbc-9807-e7c64eab272c" alt="img" width="1100"/>
</p>

<br>

## 📃 Contexto
Este projeto tem como objetivo analisar os comentários dos clientes em uma plataforma de e-commerce para identificar o sentimento (positivo ou negativo) associado a cada avaliação. A análise de sentimentos permite extrair insights relevantes sobre a experiência dos usuários e auxilia na tomada de decisões para melhorar o atendimento, os produtos e os processos da empresa.

***

<br>

## 🛠️ Ferramentas e Tecnologias Utilizadas
**Python**
- ***Manipulação e análise de dados -** Pandas, Numpy
- **Visualização -** Matplotlib, Seaborn
- **Processamento de texto -** nltk, re, wordcloud
- **Machine Learning -** scikit-learn (Logistic Regression, Random Forest)
- **Deploy -** – Streamlit
  
***

<br>

🎯 Objetivo
Desenvolver um projeto completo de machine learning, com interface amigável para o usuário final capaz de:
- Através de arquivo .csv com comentários, gerar nuvem com principais palavras das avaliações dos clientes, dando uma visão rápida da opinião deles sobre os produtos.
- Avaliar automaticamente avaliações escritas, indicando se é positiva ou negativa, utilizando técnicas de Processamento de Linguagem Natural (PLN) e Machine Learning.

***

<br>

## 🧱 Estrutura do Projeto

#### 🔸 Entendimento e Análise Exploratória dos Dados
#### 🔸 Pré-processamento
#### 🔸 Modelagem
#### 🔸 Deploy com Streamlit
#### 🔸 Produto Final

<br>

### 📌 Entendimento e Análise Exploratória dos Dados
- Importação e análise exploratória dos dados
- Leitura de dados de avaliações de clientes
- Estatísticas sobre a quantidade de avaliações com ou sem comentários e títulos, distribuição de score

--

### 📌 Pré-processamento
- Limpeza dos textos (remoção de stopwords, tokenização, etc.)
- Vetorização com CountVectorizer e TF-IDF
- Visualizações com geração de nuvem de palavras (WordCloud)

--

### 📌 Modelagem
- Treinamento e avaliação de modelos (Regressão Logística e Random Forest)
- Métricas: Acurácia, F1-Score, Matriz de Confusão

--

###  📌 Deploy com Streamlit
- Interface interativa
- Geração de nuvem de palavras a partir de arquivo .csv com avaliações
- Análise de sentimento com base em comentário, retornando sentimento previsto (Positivo ou Negativo)

## Principais Conclusões
Aproximadamente 58% dos clientes não deixaram comentários.

Apenas 11% das avaliações possuem título.

O modelo de Regressão Logística apresentou bons resultados na classificação de sentimentos.

Os bigramas e trigramas mais frequentes indicam tendências sobre o que agrada ou desagrada os clientes (ex: "produto de qualidade", "entrega atrasada", etc.).


## ✅ Produto Final

### 🟩 Tela inicial do app
