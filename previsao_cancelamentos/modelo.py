def criacao_treinamento_modelo():
    
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    from sklearn.metrics import accuracy_score
    from sklearn.neighbors import KNeighborsClassifier
    from imblearn.over_sampling import SMOTE
    import joblib

    print('Pacotes carregados')

    df = pd.read_csv('novos_dados.csv')
    print('Colunas no CSV:', df.columns.tolist())

    # Manter apenas clientes com até 5 filhos
    df = df[df['QT_FILHOS'] <= 5]

    # Preenchendo valores nulos em QT_FILHOS com a mediana
    df['QT_FILHOS'] = df['QT_FILHOS'].fillna(df['QT_FILHOS'].median())

    # Deletar demais valores nulos e duplicados
    df = df.dropna()
    df = df.drop_duplicates()

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

    # Colunas selecionadas
    columns = [
        'FORMA_AQUISICAO', 'IDADE_CLIENTE', 'SEXO', 'QT_FILHOS', 'DIAS_ATIVO',
        'MESES_ATIVO', 'DURACAO_CONTRATO', 'VL_PLANO_ADESAO', 'VL_PLANO_ATUAL',
        'NOME_PRODUTO', 'QT_PONTOS_INSTALADOS', 'QT_PC_PAGAS', 'QT_PC_VENCIDAS',
        'QT_PC_PAGA_ATRASO', 'QT_PC_PAGA_EM_DIA', 'QT_ACORDO_PAGAMENTO',
        'VL_MENSALIDADE_ATRASO', 'VL_MENSALIDADE_DT_AQUISICAO',
        'VL_MENSALIDADE_DT_ATUAL', 'NIVEL_PAGAMENTO', 'COD_SITUACAO'
    ]

    df = df[columns]

    # Separar preditoras e alvo
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Balancear com SMOTE
    smote = SMOTE(random_state=100)
    X_res, y_res = smote.fit_resample(X, y)

    # Dividir treino/teste
    X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.3, random_state=42)

    # Padronizar
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Treinar modelo
    melhor_k = 3
    modelo = KNeighborsClassifier(n_neighbors=melhor_k)
    modelo.fit(X_train_scaled, y_train)

    # Avaliar
    acc = accuracy_score(y_test, modelo.predict(X_test_scaled))
    print(f"Acurácia: {acc:.2%}")

    # Salvar pipeline
    joblib.dump(modelo, 'modelo_churn.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    print("Modelo e scaler salvos!")

def tratar_dados_para_predicao(df):
    import pandas as pd
    from sklearn.preprocessing import LabelEncoder

    df = df.copy()
    
    # Mesmo tratamento usado no treinamento
    df = df[df['QT_FILHOS'] <= 5]
    df['QT_FILHOS'] = df['QT_FILHOS'].fillna(df['QT_FILHOS'].median())
    df = df.dropna()
    df = df.drop_duplicates()

    contrato_map = {'12 Meses': 12, '24 Meses': 24, '36 Meses': 36, '48 Meses': 48}
    df['DURACAO_CONTRATO'] = df['DURACAO_CONTRATO'].replace(contrato_map)
    df = df.reset_index(drop=True)

    df.loc[df.QT_PC_PAGAS > df.DURACAO_CONTRATO, 'QT_PC_PAGAS'] = df.DURACAO_CONTRATO
    df.loc[df.QT_PC_PAGA_EM_DIA > df.DURACAO_CONTRATO, 'QT_PC_PAGA_EM_DIA'] = df.DURACAO_CONTRATO

    bins = [-100, 3, 6, 12, 48]
    labels = ['RASO', 'BAIXO', 'MEDIO', 'ALTO']
    df['NIVEL_PAGAMENTO'] = pd.cut(df['QT_PC_PAGAS'], bins=bins, labels=labels)

    lb = LabelEncoder()
    for col in ['SEXO', 'FORMA_AQUISICAO', 'NOME_PRODUTO', 'NIVEL_PAGAMENTO']:
        df[col] = lb.fit_transform(df[col].astype(str))

    colunas_modelo = [
        'FORMA_AQUISICAO', 'IDADE_CLIENTE', 'SEXO', 'QT_FILHOS', 'DIAS_ATIVO',
        'MESES_ATIVO', 'DURACAO_CONTRATO', 'VL_PLANO_ADESAO', 'VL_PLANO_ATUAL',
        'NOME_PRODUTO', 'QT_PONTOS_INSTALADOS', 'QT_PC_PAGAS', 'QT_PC_VENCIDAS',
        'QT_PC_PAGA_ATRASO', 'QT_PC_PAGA_EM_DIA', 'QT_ACORDO_PAGAMENTO',
        'VL_MENSALIDADE_ATRASO', 'VL_MENSALIDADE_DT_AQUISICAO',
        'VL_MENSALIDADE_DT_ATUAL', 'NIVEL_PAGAMENTO'
    ]

    return df[colunas_modelo]

if __name__ == "__main__":
    criacao_treinamento_modelo()