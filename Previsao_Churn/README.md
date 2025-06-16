

<h1 align="center">Previsão de Churn de Clientes</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/5f0649ed-982e-4bbc-9807-e7c64eab272c" alt="img" width="1100"/>
</p>

<br>

## 📃 Contexto

Empresas que operam com planos mensais (como operadoras, serviços de assinatura, academias etc.) enfrentam o desafio constante de **reter clientes**. Antecipar o risco de churn permite ações preventivas mais eficazes, como ofertas personalizadas ou campanhas de engajamento.  
Este projeto tem como objetivo **prever o churn de clientes** com base em informações contratuais, comportamentais e financeiras, utilizando **algoritmos de Machine Learning** e uma **interface desenvolvida em Streamlit**.

***

<br>

## 🛠️ Tecnologias e Ferramentas Utilizadas
**Python**
- **Pandas, Numpy** – Manipulação de dados
- **Scikit-learn** – Pré-processamento, modelagem, avaliação
- **Imbalanced-learn (SMOTE)** – Balanceamento de classes
- **Joblib** – Serialização do modelo
- **Streamlit** – Interface interativa para previsão
- **Excel / CSV** – Entrada e saída de dados

***

<br>

## 🎯 Objetivo

Desenvolver um projeto completo de machine learning capaz de:
- **Analisar dados históricos** de clientes
- **Identificar padrões de evasão**
- **Prever o churn futuro**
- Disponibilizar essas previsões de forma acessível via **aplicativo web**

***

<br>

## 🧱 Estrutura do Projeto

#### 🔸 Entendimento dos dados
#### 🔸 Engenharia de Atributos
#### 🔸 Pré-processamento
#### 🔸 Modelagem
#### 🔸 Deploy com Streamlit
#### 🔸 Produto Final

***

<br>

### 📌 Entendimento dos Dados
- Análise de variáveis como idade, tempo de contrato, pagamentos, pontuação etc.
- Identificação de valores ausentes e outliers.

***

<br>

### 📌 Engenharia de Atributos
- Conversão de variáveis categóricas com `LabelEncoder`.
- Criação de nova variável **NIVEL_PAGAMENTO**, com base na quantidade de parcelas pagas.

***

<br>

### 📌 Pré-processamento
- Imputação de valores nulos com mediana ou valores padrão.
- Correção de valores inconsistentes (ex: parcelas pagas acima do contrato).
- Padronização dos dados com `StandardScaler`.

***

<br>

### 📌 Modelagem
- Modelo escolhido: **K-Nearest Neighbors (KNN)**
- Balanceamento da base com **SMOTE** para lidar com a classe minoritária (`CHURN = 1`).
- Avaliação com **accuracy** e outras métricas.
  
***

<br>

### 📌 Deploy com Streamlit
- Criação de um app interativo onde o usuário:
  - Faz upload de um CSV com os dados de clientes.
  - Visualiza a prévia dos dados.
  - Gera previsões com um clique.
  - Baixa um arquivo Excel com o resultado.

***

<br>

## ✅ Resultado Final

### 🟩 Tela inicial do app

<p align="center">
  <img src="https://github.com/user-attachments/assets/0f194369-0ab5-4f97-862d-cf462e32cd0b" alt="img" width="1000"/>
</p>

