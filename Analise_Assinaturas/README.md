<h1 align="center">📊 Análise de Vendas - Serviços de Assinatura</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/182b2b08-47ba-4512-9daf-1911b2c04fe5" alt="analise_vendas" width="1100" height="330"/>
</p>

<br>

## 📃 Contexto
A área comercial de uma empresa fictícia de serviços de assinatura deseja compreender seu desempenho no mês. Os objetivos incluem entender os principais fatores que impactam o faturamento e a percepção dos clientes sobre produtos e atendimento, a fim de orientar melhorias estratégicas no setor comercial.

***

<br>

## 🛠️ Ferramentas e Métodos Utilizados
- Microsoft Excel (fórmulas, tabelas dinâmicas, gráficos, slicers)
- Tratamento dos dados (formatação, engenharia de atributos)
- Business Intelligence

***

<br>

## 🎯 Objetivos
A análise busca, além de diagnosticar o desempenho mensal da empresa, identificar oportunidades para aumentar o faturamento e a satisfação dos clientes. As perguntas que guiarão nossa análise são:

- Qual foi o faturamento do mês?
- Que serviço é o mais adquirido?
- Qual é o perfil dos clientes?
- Qual a avaliação dos serviços?
  
***

<br>

## 🧱 Estrutura do Projeto
### 🗄 Banco de Dados

| Coluna           | Descrição |
|------------------|-----------|
| CPF              | CPF do cliente                                                |
| Nome             | Nome completo                                                 |
| Genero           | Gênero (masculino ou feminino)                                |
| Nivel_Estudos    | Formação (médio, superior, pós-graduação, mestrado, doutorado)|
| Interesse/Hobby  | Interesses/Hobbies                                            |
| Regiao           | Estado de residência                                          |
| Data_Nasc        | Data de nascimento                                            |
| Idade            | Idade                                                         |
| Faixa_Etaria     | Faixa etária                                                  |
| Avaliacao        | Avaliação dada ao serviço                                     |
| Assinatura       | Tipo de serviço contratado                                    |
| Mensalidade      | Valor mensal do serviço                                       |

***

<br>

### 📍 Respondendo às perguntas de negócio

#### 📌 1. Qual foi o faturamento do mês?  
O faturamento foi de **R$26.467,80**. Mantido esse ritmo, o ano pode fechar com aproximadamente **R$300.000**.

--
  
#### 📌 2. Que serviço é o mais adquirido?**  
O produto que conta com mais assinantes é o **Magic Box, 35% do total de assinaturas**. Consideremos o total de assinaturas por serviço e seus respectivos impactos no faturamento:

| Serviço     | Valor (R$)          | Total Assinaturas     | Faturamento     |
|:-----------:|:-------------------:|:---------------------:|:---------------:|
| Deluxe Box  | R$35,90             | 168                   | R$6.031,20      |
| Magic Box   | R$9,90              | 266                   | R$2.633,40      |
| Premium X   | R$79,90             | 136                   | R$10.866,40     |
| Safe Watch  | R$29,90             | 232                   | R$6.936,80      |
| **Total**   | --                  | **802**               | **R$26.467,80** |

**Insight:** Serviços de menor valor concentram a maior parte das assinaturas, mas têm menor peso no faturamento. Notamos que, apesar de contar com o maior número de assinaturas, Magic Box é o produto com menor impacto no faturamento.

--

#### 📌 3. Qual o perfil dos clientes?**  
Atualmente, contamos com **802 assinantes**. Considerando o estado em que moram, a maior parte deles é do **Rio Grande do Sul (51%)**, seguido do **Paraná (27%)** e **Santa Catarina (22%)**. De acordo com o gênero e faixa etária, a maior parte dos nosso clientes é do **sexo masculino**. A faixa etária predominante é de **35-44 e 54-70, para ambos os sexos**.

**Total de assinantes:** 802

**Distribuição geográfica:**
- Rio Grande do Sul – 51%
- Paraná – 27%
- Santa Catarina – 22%

**Gênero predominante:** Masculino

**Faixas etárias predominante:** 35–44 e 54–70 (ambos os sexos)

--

#### 📌 4. Qual a avaliação dos serviços?
Avaliação geral positiva. As principais queixas envolvem:
- Falta de itens
- Atrasos na entrega
- Embalagens danificadas
- Suporte ruim

***

<br>

### 📈 Recomendações Estratégicas
De acordo com a análise dos dados, segue sugestões de ações para melhorias:

#### 🟦 Relativas ao faturamento:
* **Oferecer upgrades de planos:** Incentivar migração para planos como o Premium X, destacando seus diferenciais.

* **Expandir presença no PR e SC:** Campanhas regionais, sistema de indicação e promoções específicas para atrair novos clientes.

* **Investir nos perfis com maior adesão:** Público 35–44 e 54-70 anos, de ambos os sexos. Coletar feedbacks desse grupo pode guiar campanhas mais assertivas.

--

#### 🟦 Relativas ao tendimento:
* **Revisar processos de entrega:** Garantir testes de qualidade, verificação de itens e avaliar performance da transportadora.

* **Aprimorar o suporte ao cliente:** Avaliar tempo e eficácia nas respostas, oferecer soluções que gerem satisfação (ex: descontos, trocas ágeis de danificados).

***

<br>

*Este projeto foi desenvolvido como parte do meu portfólio em análise de dados. Sinta-se à vontade para explorar os dados, sugerir melhorias ou entrar em contato!*
