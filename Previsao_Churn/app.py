import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from io import BytesIO
import joblib

# -- Carregando modelo e padronizador ---
modeloFinal = joblib.load('modelo_knn.pkl')
padronizador = joblib.load('padronizador.pkl')

# -- Função de tratamento de dados
def tratar_dados_para_predicao(df):

    # Manter apenas clientes com até 5 filhos
    df = df[df['QT_FILHOS'] <= 5]

    # Preenchendo valores nulos em QT_FILHOS com a mediana
    df['QT_FILHOS'] = df['QT_FILHOS'].fillna(df['QT_FILHOS'].median())

    # Converter texto para números em DURACAO_CONTRATO
    contrato_map = {'12 Meses': 12, '24 Meses': 24, '36 Meses': 36, '48 Meses': 48}
    df['DURACAO_CONTRATO'] = df['DURACAO_CONTRATO'].replace(contrato_map)

    # Resetar índice
    df = df.reset_index(drop=True)

    # Corrigir outliers
    df.loc[df.QT_PC_PAGAS > df.DURACAO_CONTRATO, 'QT_PC_PAGAS'] = df.DURACAO_CONTRATO
    df.loc[df.QT_PC_PAGA_EM_DIA > df.DURACAO_CONTRATO, 'QT_PC_PAGA_EM_DIA'] = df.DURACAO_CONTRATO

    # Criar nível de pagamento
    bins = [-100, 3, 6, 12, 48]
    labels = ['RASO', 'BAIXO', 'MEDIO', 'ALTO']
    df['NIVEL_PAGAMENTO'] = pd.cut(df['QT_PC_PAGAS'], bins=bins, labels=labels)

    # Codificar variáveis categóricas
    lb = LabelEncoder()
    for col in ['SEXO', 'FORMA_AQUISICAO', 'NOME_PRODUTO', 'NIVEL_PAGAMENTO']:
        df[col] = lb.fit_transform(df[col].astype(str))

    # Seleção de colunas
    columns = [
        'FORMA_AQUISICAO', 'IDADE_CLIENTE', 'SEXO', 'QT_FILHOS', 'DIAS_ATIVO',
        'MESES_ATIVO', 'DURACAO_CONTRATO', 'VL_PLANO_ADESAO', 'VL_PLANO_ATUAL',
        'NOME_PRODUTO', 'QT_PONTOS_INSTALADOS', 'QT_PC_PAGAS', 'QT_PC_VENCIDAS',
        'QT_PC_PAGA_ATRASO', 'QT_PC_PAGA_EM_DIA', 'QT_ACORDO_PAGAMENTO',
        'VL_MENSALIDADE_ATRASO', 'VL_MENSALIDADE_DT_AQUISICAO',
        'VL_MENSALIDADE_DT_ATUAL', 'NIVEL_PAGAMENTO'
    ]

    df = df[columns]

    # Deletar valores nulos e duplicados
    df = df.dropna()
    df = df.drop_duplicates()

    return df

# -- Interface Streamlit
st.markdown(
    "<h1 style='text-align: center;'>📉 Previsão de Churn</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'><i>App para previsão de Churn em serviços de assinatura</i></p>",
    unsafe_allow_html=True
)

st.divider()

st.write("")
st.write("Faça upload de um arquivo CSV com os dados dos clientes para prever o churn")

arquivo = st.file_uploader("📤 Fazer upload do arquivo CSV", type=["csv"])

if arquivo is not None:
    dados = pd.read_csv(arquivo, sep=';')
    st.write("Prévia dos dados:")
    st.dataframe(dados.head())


    if st.button("Gerar Previsões"):
        with st.spinner("Gerando previsões, por favor aguarde..."):
            try:
                # TRATAMENTO
                dados_tratados = tratar_dados_para_predicao(dados)

                # PADRONIZAR
                dados_pad = padronizador.transform(dados_tratados)

                # PREVER
                previsoes = modeloFinal.predict(dados_pad)

                dados['CHURN_PREVISTO'] = pd.NA  # cria a coluna com NaN para todas as linhas

                # preenche previsões só nas linhas válidas (com índices de dados_tratados)
                dados.loc[dados_tratados.index, 'CHURN_PREVISTO'] = previsoes

                # GERAR EXCEL PARA DOWNLOAD
                buffer = BytesIO()
                dados.to_excel(buffer, index=False)
                buffer.seek(0)

                st.success("Previsões geradas com sucesso!")
                st.download_button("⬇️ Baixar Excel com Previsões", buffer, file_name="previsoes_churn.xlsx")

            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")
