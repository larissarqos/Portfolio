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

***

<br>

## 📋 Principais Conclusões
**Satisfação**  
De acordo com os unigramas e e trigramas, podemos afirmar que a **maioria dos clientes ficou satisfeita com o serviço de entrega e qualidade dos produtos**.  
De maneira geral, a maior das avaliações (positivas e negativas) são relativas à entrega e qualidade dos produtos. Focar na agilidade de entrega pode ser um ponto crucial.

--

**Comentários**  
Após a remoção de valores nulos, temos que cerca de 9.000 avaliações com 1 estrela e pouco mais de 20.000 com 5 estrelas, o que indica:
- Aproximadamente **36% dos clientes que deram 5 estrelas escreveram um comentário**.
- Aproximadamente **77% dos clientes que deram 1 estrela escrevem um comentário**. Um cliente é mais propenso a comentar quando está insatisfeito com o produto.

--

**Palavras por comentário**  
A maioria dos comentários tem **até 10 palavras, com pico no intervalo 2-5 palavras**. Como vimos nos trigramas, 3 palavras já são suficientes para entender o sentimento do cliente. Seria interessante, na seção de avaliações, **pedir um mínimo de 5 palavras para estimar o cliente a deixar seu comentário**, mesmo que curto.

--

**Acurácia do Modelo**  
Nosso modelo obteve quase 95% de acurácia

***

<br>

## ✅ Produto Final
Abaixo, prints da tela do app gerado via streamlit, com as opções de gerar nuvem de palavras e analisar comentário como positivo ou negativo.

<br>

### 🟩 Tela - Gerar nuvem de palavras

<p align="center">
  <img src="https://github.com/user-attachments/assets/0d613918-de8f-48cd-9a9e-b16303a9801b" alt="img" width="800"/>
</p>

--

### 🟩 Após inserção do arquivo
<p align="center">
  <img src="https://github.com/user-attachments/assets/52d9aae6-432b-4597-b663-b15fc26e946f" alt="img" width="800"/>
</p>

-- 

### 🟩 Nuvem Gerada
<p align="center">
  <img src="https://github.com/user-attachments/assets/62b75633-7084-4924-8f25-35818ee9d945" alt="img" width="800"/>
</p>

<br>

-- 

### 🟩 Tela - Análise de sentimento em comentário
<p align="center">
  <img src="https://github.com/user-attachments/assets/c5aea59d-3c91-4944-b175-a3075974576e" alt="img" width="800"/>
</p>

--

### 🟩 Resultado Positivo
<p align="center">
  <img src="https://github.com/user-attachments/assets/db9e9c44-6b67-47b2-8482-3f42c7771788" alt="img" width="800"/>
</p>

--

### 🟩 Resultado Negativo
<p align="center">
  <img src="https://github.com/user-attachments/assets/f77ecca0-bdef-4564-bf41-5e6f7decfcef" alt="img" width="800"/>
</p>
