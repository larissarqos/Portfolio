<h1 align="center"> Análise de Performance e Satisfação de Colaboradores</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/e2972ec8-ad68-423f-9563-f97916d0cbd7" alt="img" width="1100"/>
</p>

<br>

## 📃 Contexto 
Neste projeto, faremos a **análise de performance de funcionários e suas avaliações em relação à satisfação com a empresa**. O objetivo é ajudar o setor de RH a **detectar que fatores estão relacionados ao baixo desempenho e satisfação** no ambiente de trabalho e que **medidas podem ser adotadas para melhorar esses resultados**. Começaremos com uma **análise exploratória dos dados**, partindo para a **captura de insights** úteis para nossa análise e por fim uma série de **recomendações** com base nas conclusões obtidas.

Você pode consultar o dashboard no Power BI em anexo (Dashboard/Dashboard_RH.pbix), ou através do [link](https://app.powerbi.com/reportEmbed?reportId=34679753-5135-46d0-b0a4-fd2906a8b876&autoAuth=true&ctid=50ac28df-71ea-410c-add9-15b6381786db).

***

<br>

## 🛠️ Ferramentas e Métodos Utilizados
### 🔸 Métodos
- Limpeza e tratamento de dados
- Análise exploratória
- Engenharia de atributos
- Análise descritiva, diagnóstica e prescritiva

### 🔸 Ferramentas
- Excel (fonte de dados)
- Power BI (visualização)
  
***

<br>

## 🎯 Objetivos 
O foco do projeto é entregar recomendações que podem ajudar o RH a melhorar a satisfação e desempenho dos funcionários da empresa.

***

<br>

## 🧱 Estrutura do Projeto

#### 🔸 Banco de Dados
#### 🔸 Compreendendo os Dados
#### 🔸 Insights Obtidos
#### 🔸 Recomendações Estratégicas

***

<br>

### 🗄 Banco de dados
A base de dados está em inglês e possui a tabela analytics_data. Estão listadas aqui apenas as colunas que foram utilizadas na análise.

| Coluna | Descrição | Tipo de Dado |
|----------|----------|----------|
| city_id | ID da cidade  | varchar(15), chave primária da tabela  |
| city_name   | Nome da cidade   | varchar(20)  |
| population   | Quantidade de habitantes  |  bigint |
| estimated_rent  | Valor estimado do aluguel   | float  |
| city_rank  | Ranking das cidades  | int  |


***

<br>


### 📍 Compreendendo os Dados
Aqui, vamos analisar as diferentes partes que compoem a empresa e suas características, sendo elas: o perfil dos funcionários e os setores da empresa.

#### 📌 Perfil dos funcionários
A empresa possui **1470 funcionários**. Considerando suas características de **gênero**, **estado civil** e **faixa etária**, temos:

**Gênero -** Maioria é do gênero masculino.
- **Homens:** 60%
- **Mulheres:** 40%

<br>

**Estado Civil -** Maioria é casado.
- **Casado:** 46%
- **Solteiro:** 32%
- **Divorciado:** 22%

<br>

**Faixa Etária -** Maioria entre 31-50 anos.
- **31-40:** 42%
- **41-50:** 22%
- **26-30:** 18%
- **50+:** 10%
- **18-25:** 8%

--

#### 📌 Relação com a empresa
Sobre sua relação com a empresa, considerando departamento, anos de serviço, nível de desempenho e satisfação, temos:

**Departamento -** Research & Development possui 65% dos funcionários.
- **Research & Development:** 65%
- **Human Resources:** 30%
- **Sales:** 4%

<br>

**Anos na Serviço -** Maior parte está entre 0 e 7 anos na empresa.
- **4-7:** 32%
- **0-3:** 32%
- **8-10:** 19%
- **11-15:** 7%
- **16-20:** 5%
- **20+:** 4%

<br>

**Performance -** A maior parte dos funcionários possui bons resultados em performance.
- **Alta:** 85%
- **Baixa:** 15%
  
<br>

**Nível Satisfação -** Quase 40% dos funcionários está muito satisfeito com a empresa. Média e Baixa satisfação se encontram praticamente empatados.
- **Alto:** 39%
- **Médio:** 30%
- **Baixo:** 31%

--

#### 📌 Departamentos
A empresa possui 3 departamentos: Human Resources, Research & Development e Sales. Vamos verificar algumas informações por departamento, conforme tabela:

| Departamento | Total Funcionários | Média Anos na Empresa | Média Anos Desde Ult. Promoção | Total para Promover | Total para Desligar|
|--------------|--------------------|-----------------------|--------------------------------|---------------------|--------------------|
| Human Resources        | 63       | 7,24                  | 1,78                           | 2                   | 1                  |
| Research & Development | 961      | 6,86                  | 2,14                           | 38                  | 11                 |
| Sales                  | 446      | 7,28                  | 2,35                           | 16                  | 10                 |

<br>

Considerando os níveis de satisfação e performance por departamento, temos:

| Departamento           | Alta Satisfação | Média Satisfação | Baixa Satisfação | Alta Performance | Baixa Performance |
|------------------------|-----------------|------------------|------------------| -----------------|-------------------|
| Human Resources        | 49%             | 24%              | 27%              | 86%              | 14%               |
| Research & Development | 38%             | 31%              | 31%              | 84%              | 16%               |
| Sales                  | 39%             | 28%              | 33%              | 86%              | 14%               |

***

<br>

#### 💡 Insights Obtidos  
Com base nos dados, podemos tirar algumas conclusões em relação à performance e satisfação dos colaboradores. 

*Obs.: Os insights foram obtidos com base na análise dos dados através dos gráficos. Por favor, abrir o dashboard no Power BI para acompanhar as conclusões.*

#### 🟨 Baixa Performance
- **Gênero e Faixa Etária:** Os fatores de gênero e faixa etária não têm diferença significativa nos resultados de performance, ambos apresentaram valores semelhantes. A **principal diferença se dá na faixa dos 50+, para o gênero feminino, em que 20% das colaboradoras está com baixo rendimento**, comparado ao geral da empresa com 14% de funcionários em baixo desempenho.

- **Tempo de Serviço:** Há um crescimento sutil no baixo desempenho com o passar dos anos de serviço, o pico se dá na faixa dos 11-15 anos na empresa. Enquanto os demais períodos se encontram próximos à média geral, **11-15 possui 22% do total com baixo desempenho**, que passa a melhorar com o tempo, chegando a 12% na faixa dos 20+ anos de trabalho.

- **Departamento:** Dentre os departamentos, **Research & Development possui 16% dos colaboradores com baixo rendimento**, isso se acentua para o período de **11-15 anos de serviço, indo para 28%**. Sobe para **33% quando consideramos apenas o gênero masculino**.

--

#### 🟨 Alta Performance
- **Tempo de Serviço:** Funcionários com **0-3 anos de serviço** têm melhor desempenho, especialmente nos setores de **Human Resources (90%) e Sales (93%)**. **Research & Development possui 86% dos colabores com alto desempenho** para esse período.
Para o perfil com **mais de 20 anos na empresa, Research & Development possui a parcela 93% com alta performance**, enquanto os demais setores estão na faixa dos 80%.

--

#### 🟨 Baixa Satisfação
- **Gênero e Faixa Etária:** Em comparação com a média geral, não há grande disparidade no nível de satisfação por gênero ou faixa etária. 

- **Tempo de Serviço:** No geral, a maior parte dos funcionários com 0 a 15 anos de serviço indicou baixa satisfação em relação à empresa. Colaboradores com 11-15 anos de serviço têm maior soma de insatisfação, 37% do total.

- **Departamento:** Os departamentos de Sales e Research & Development possuem a maior quantidade de funcionários não satisfeitos**. Em termos de proporção, juntos eles representam **30% dos colaboradores** insatisfeitos, com HR somando apenas 1,6% desse total. Para além disso, também possuem maior percentual de funcionários prontos para promoção.

- **Tempo para Promoção:** Associada às baixas avaliações está também a média de tempo para promoção, que pesa especialmente para o setor de Sales, que possui maior parte de insatisfeitos com **33% de colaboradores do setor** e tempo médio de **2,35 anos**, contra 1,78 de HR, mesmo ambos contando com os mesmos valores de desempenho.

--

#### 🟨 Alta Satisfação
- **Tempo de Serviço:** Os colaboradores com +20 anos de serviço possuem maior contentamento em relação a empresa, 45% indicou alta satisfação.

- **Departamento:** Human Resources é o setor mais satisfeito na empresa (e também o com menor tempo médio para promoção).

***

<br>

### 🚀 Recomendações Estratégicas
Com base na análise dos dados e padrões identificados, algumas ações podem ser adotadas, de acordo com os principais pontos avaliados: Performance dos colaboradores e satisfação deles em relação à empresa.

#### 🟦 Performance
**Sistemas de reconhecimento e desenvolvimento, ginástica laboral:** De acordo com os dados, a performance dos funcionários, no geral, cai percentualmente ao longo dos anos, e isso, dado o cenário dos dados, pode estar associado especialmente à

- Falta de motivação ou perspectiva de crescimento na empresa 
- Rotina desgastante 
- Gestão ausente ou falha nos setores da empresa

Para melhorar o desempenho dos funcionários, considerando os pontos acima, pode-se implementar:
- **Falta de motivação ou perspectiva de crescimento na empresa:** **Reconhecer a contribuição dos funcionários** não apenas com promoções, mas **feedbacks públicos**, sejam eles **reuniões mensais com premiações**, **murais em áreas convivência**, **menções** assim como oferecer **planos de desenvolvimento individual** e **programas de treinamento internos ou externos**. Tudo isso levará o colaborador a dar o seu melhor, ampliando também sua perspectiva de crescimento dentro da empresa.

- **Rotina desgastante:** Dias de **ginástica laboral**, **short friday** ou um **dia da semana sem reuniões** podem tornar o dia de trabalho menos tenso, levando a um melhor desempenho nas atividades diárias.

- **Gestão ausente ou falha nos setores da empresa** Gestores atentos escutam os colaboradores. **Atentar-se às suas reclamações**, **implementar indicadores de performance específicos para cada setor**, pode melhor seu rendimento, pois estarão de acordo com suas especificações.

--

#### 🟦 Satisfação
**Alinhar expectativas, criar planos de carreira:** Pudemos notar que o tempo de serviço e nível de insatisfação estão muito interligados, com maior parte de descontentes na faixa dos 0-15 anos. Seguindo os insights nos dados, os níveis de insatisfação podem estar relacionados à

- Quebra de expectativa de funcionários novatos
- Sensação de estagnação / não reconhecimento na empresa

Para solucionar essas possíveis queixas, pode-se:

- **Quebra de expectativa de funcionários novatos:** Melhorar a experiência de onboarding, com acompanhamento constante e plano de carreira já pré-definidos, isso pode alinhar as expectativas dos novos funcionários, fazendo-os entender o que esperar da empresa e como podem crescer nela.

- **Sensação de estagnação / não reconhecimento na empresa:** Muito próximos aos problemas de desempenho, esse pontos podem resolvidos incluindo a **participação dos colaboradores em projetos de melhoria** nos seus respectivos setores, aderir a ** bonificações / premiações** para funcionários de melhor desempenho e oferecer programas de carreira dentro da empresa. Tudo isso pode colaborar a uma maior sensação de crescimento e valorização na corporação por parte dos funcionários.
  
***

<br>

*Este projeto foi desenvolvido como parte do meu portfólio em análise de dados. Sinta-se à vontade para explorar os dados, sugerir melhorias ou entrar em contato!*
