<h1 align="center">Análise de Satisfação de Clientes de E-commerce</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/16ef9636-8525-4d00-ac6f-6f9c75cb2a87" alt="img" width="1100"/>
</p>

<br>

## 📃 Contexto
Este projeto tem como objetivo aplicar técnicas de Processamento de Linguagem Natural (PLN) e Machine Learning para identificar o sentimento dos clientes a partir de suas avaliações em uma plataforma de e-commerce.

***

<br>

## 🛠️ Ferramentas e Tecnologias Utilizadas
**Python**
- **Manipulação e análise de dados -** Pandas, Numpy
- **Visualização -** Matplotlib, Seaborn
- **Processamento de texto -** nltk, re, wordcloud
- **Machine Learning -** Scikit-learn (Logistic Regression, Random Forest)
- **Deploy -** Streamlit

***

<br>

## 📋 Metodologia: CRISP-DM

A estrutura do projeto segue a metodologia CRISP-DM (Cross Industry Standard Process for Data Mining), composta por 6 etapas:
  1. Entendimento do Negócio
  2. Entendimento dos Dados
  3. Preparação dos Dados
  4. Modelagem
  5. Avaliação do Modelo
  6. Deploy

***

<br>

### 📌 Entendimento do Negócio
O objetivo principal é **classificar avaliações de clientes como positivas ou negativas**, utilizando o texto fornecido nos comentários. Os insights extraídos servirão para:

- Identificar fatores de satisfação e insatisfação.
- Apoiar decisões de melhoria de produto e serviço.
- Automatizar o monitoramento de reputação da marca.

---

<br>

### 📌 Entendimento dos Dados
O conjunto de dados contém informações sobre:
- Avaliações de clientes.
- Títulos e textos dos comentários.
- Notas atribuídas (de 1 a 5 estrelas).

Durante a exploração inicial, observamos:

- Muitos valores ausentes em comentários e títulos.
- Apenas 41% dos clientes deixaram algum texto.
- Clientes insatisfeitos (nota 1) tendem mais a comentar do que os satisfeitos (nota 5).

---

<br>

### 📌 Preparação dos Dados

As principais etapas de limpeza e preparação foram:

- Remoção de valores nulos.
- Redefinição de índices.
- Tokenização e vetorização de textos com `CountVectorizer`.
- Geração de unigramas e trigramas para análise de frequência.
- Criação de variável alvo binária com base nas notas de score: Notas 4 e 5 = 1, Positivo; Notas 1 e 2 = 0, Negativo.

---

<br>

### 📌 Modelagem

- Modelo escolhido: **Regressão Logística**
- Vetorização dos dados com `CountVectorizer`.
- Separação entre treino e teste.
- Treinamento da máquina preditiva com os textos processados.

---

<br>

### 📌 Avaliação

Avaliação do modelo com as seguintes métricas:

- **Acurácia:** 92.85%
- **F1 Score:** 95.00%
- **Matriz de Confusão:**

  ```
  [[1860  307]
   [ 228 5089]]
  ```

<br>

**O que isso significa?** 
O modelo apresenta excelente desempenho, com precisão de previsões e recall equilibrados. Erra um pouco mais ao ao confundir uma frase negativa como se fosse positiva. Modelo será otimizado em versões futuras, com aplicação de outros algortimos, como Random Forest ou SVM, a fim de avaliar e melhorar sua performance.

---


<br>

### 📌 Deploy
O deploy do modelo foi feito com Streamlit. A interface intuitiva do app permite:
- Gerar de nuvem de palavras a partir de arquivo .csv com avaliações, permitindo uma visão rápida dos principais pontos comentados em novas avaliações.
- Análise de sentimento com base em comentário, retornando sentimento previsto (Positivo ou Negativo).

<br>

#### Prints do produto final:

#### 🟩 Opção gerar nuvem de palavras

<p align="center">
  <img src="https://github.com/user-attachments/assets/0d613918-de8f-48cd-9a9e-b16303a9801b" alt="img" width="800"/>
</p>

--

<br>

#### 🟩 Após inserção do arquivo
<p align="center">
  <img src="https://github.com/user-attachments/assets/52d9aae6-432b-4597-b663-b15fc26e946f" alt="img" width="800"/>
</p>

-- 

#### 🟩 Nuvem Gerada
<p align="center">
  <img src="https://github.com/user-attachments/assets/62b75633-7084-4924-8f25-35818ee9d945" alt="img" width="800"/>
</p>

<br>

-- 

#### 🟩 Opção: Análise de sentimento em comentário
<p align="center">
  <img src="https://github.com/user-attachments/assets/c5aea59d-3c91-4944-b175-a3075974576e" alt="img" width="800"/>
</p>

--

#### 🟩 Resultado Positivo
<p align="center">
  <img src="https://github.com/user-attachments/assets/db9e9c44-6b67-47b2-8482-3f42c7771788" alt="img" width="800"/>
</p>

--

<br><br>

### 📑 Principais conclusões com base em toda a análise dos dados
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

