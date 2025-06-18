

<h1 align="center">Previsão de Churn de Clientes</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/5f0649ed-982e-4bbc-9807-e7c64eab272c" alt="img" width="1100"/>
</p>

<br>

## 📃 Contexto
Nesse projeto, vamos criar um modelo de previsão de churn de clientes com base em seu perfil, informações contratuais e financeiras, utilizando algoritmos de Machine Learning. A análise dos dados e o modelo preditivo podem ser usados para entender os perfis com maior possibilidade de churn, melhorando estratégias em campanhas de marketing, bem como otimização de produtos e serviços com maior quantidade de cancelamentos.

***

<br>

## 🛠️ Tecnologias e Ferramentas Utilizadas
**Python**
- **Manipulação de dados -** Pandas, Numpy
- **Visualização -** Matplotlib, Seaborn
- **Balanceamento -** Imbalanced-learn (SMOTE)
- **Machine Learning -** Scikit-learn (KNeighborsClassifier)

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
O objetivo principal é **gerar previsões de churn com base em dados dos clientes**. Os insights extraídos servirão para:

- Prever o churn de acordo com o perfil dos cliente
- Dar suporte à tomada de decisões em campanhas de retenção de clientes
- Dar suporte a decisões de melhoria de produto e serviço.

---

<br>

### 📌 Entendimento dos Dados
O conjunto de dados contém informações sobre:
- Dados dos clientes
- Dados do tipo de plano assinado
- Dados relacionados ao pagamento do plano

Durante a exploração inicial, observamos:
- Mais de 90% das assinaturas é de duração 48 meses
- Mais de 60% das assinaturas é do plano básico (30 CANAIS HD)
- A maior parte das aquisições do serviço se deu pelo site. Aquisições por vendendor são menores e possuem maior taxa de cancelamentos
- Dado o período avaliado, a taxa de churn é de quase 26%

---

<br>

### 📌 Preparação dos Dados
As principais foram:

- Tratamento e remoção de valores nulos
- Tratamento de outliers
- Redefinição de index
- Engenharia de atributos


### 📌 Modelagem

- Codificação de variáveis categóricas (convertê-las em numéricas)
- Balanceamento das variáveis
- Separação de dados entre treino e teste
- Padronização dos dados
- Modelo escolhido: **K-Nearest Neighbors (KNN)**

---

<br>

### 📌 Avaliação
A avaliação do modelo KNN, variando o valor de k entre 3 e 9 para identificar o melhor desempenho na classificação dos dados, resultou em:

| Valor de k | Acurácia |
|------------|----------|
| k = 3      | 97,69%   |
| k = 5      | 97,38%   |
| k = 7      | 97,20%   |
| k = 9      | 97,03%   |

<br>

**O que isso significa?**   
O melhor desempenho foi obtido com **k = 3**, indicando que uma vizinhança menor resultou em maior capacidade de generalização para esse conjunto de dados. No geral, todos os valores de k testados apresentaram acurácias elevadas e consistentes, acima de 95%.

---

<br>

### 📌 Deploy
O deploy do modelo foi feito com Streamlit. A interface intuitiva do app permite:
- Gerar um arquivo .xlsx com previsão de churn para cada cliente, a partir de arquivo .csv com seus dados. 

<br>

### Prints do produto final:

#### 🟩 Tela inicial do app
<p align="center">
  <img src="https://github.com/user-attachments/assets/55fae0d8-3c6c-4455-b7c1-4e07b5198ccb" alt="img" width="800"/>
</p>

--

<br>


#### 🟩 Após upload do arquivo .csv

<p align="center">
  <img src="https://github.com/user-attachments/assets/e2e7baaf-ddfb-40ef-a869-bf0199f7204a" alt="img" width="800"/>
</p>

--

<br>

### 🟩 Gerando previsões

<p align="center">
  <img src="https://github.com/user-attachments/assets/f3eb135e-a6e3-407c-af8e-44cd0e9a689c" alt="img" width="800"/>
</p>

--

<br>


### 🟩 Previsão pronta para baixar

<p align="center">
  <img src="https://github.com/user-attachments/assets/2c248359-f106-45eb-9a0f-fe5af234f9ac" alt="img" width="800"/>
</p>

--

<br>


### 🟩 Arquivo final
Em anexo, está arquivo gerado com as previsões: *previsoes_churn.xlsx*. A coluna **CHURN_PREVISTO** contém as previsões, sendo:
- **0 =** Não churn
- **1 =** Churn
