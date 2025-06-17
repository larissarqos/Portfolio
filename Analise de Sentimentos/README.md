🛒 Análise de Satisfação de Clientes de E-commerce
Este projeto tem como objetivo analisar os comentários dos clientes em uma plataforma de e-commerce para identificar o sentimento (positivo ou negativo) associado a cada avaliação. A análise de sentimentos permite extrair insights relevantes sobre a experiência dos usuários e auxilia na tomada de decisões para melhorar o atendimento, os produtos e os processos da empresa.

🎯 Objetivo
Avaliar automaticamente o sentimento por trás das avaliações escritas por clientes, utilizando técnicas de Processamento de Linguagem Natural (PLN) e Machine Learning.

🧰 Tecnologias e Ferramentas Utilizadas
Linguagem: Python 3.x

Bibliotecas de análise de dados: pandas, numpy, matplotlib, seaborn

Processamento de texto: nltk, re, wordcloud

Machine Learning: scikit-learn (Logistic Regression, Random Forest)

Visualização: matplotlib, seaborn, WordCloud

Interface interativa (extra): Streamlit (caso esteja integrado)

⚙️ Funcionalidades
Importação e análise exploratória dos dados

Leitura de dados de avaliações de clientes

Estatísticas sobre a quantidade de avaliações com ou sem comentários e títulos

Pré-processamento de texto

Limpeza dos textos (remoção de stopwords, tokenização, etc.)

Vetorização com CountVectorizer e TF-IDF

Visualizações

Geração de nuvem de palavras (WordCloud)

Gráficos de unigramas, bigramas e trigramas

Modelagem

Treinamento e avaliação de modelos (Regressão Logística e Random Forest)

Métricas: Acurácia, F1-Score, Matriz de Confusão

Interface de Análise Interativa (se integrado com Streamlit)

Campo de texto para análise de sentimento de uma nova avaliação

Retorno do sentimento previsto (Positivo ou Negativo)

🧠 Conclusões
Aproximadamente 58% dos clientes não deixaram comentários.

Apenas 11% das avaliações possuem título.

O modelo de Regressão Logística apresentou bons resultados na classificação de sentimentos.

Os bigramas e trigramas mais frequentes indicam tendências sobre o que agrada ou desagrada os clientes (ex: "produto de qualidade", "entrega atrasada", etc.).


