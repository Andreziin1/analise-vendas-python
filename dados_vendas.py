import pandas as pd

# importando a planilha para conseguir trabalhar com os dados no pandas
df = pd.read_excel("dados/vendas_brutas_final.xlsx", sheet_name="Vendas_Brutas")

# preenchendo os clientes vazios porque não temos como descobrir o nome verdadeiro
df["cliente"] = df["cliente"].fillna("Não informado")

# preenchendo os produtos vazios porque não temos como saber qual produto foi vendido
df["produto"] = df["produto"].fillna("Não informado")

# preenchendo as categorias vazias de acordo com o produto de cada venda
df.loc[(df["categoria"].isnull()) & (df["produto"] == "Luminária"), "categoria"] = "Casa"
df.loc[(df["categoria"].isnull()) & (df["produto"] == "Monitor"), "categoria"] = "Eletrônicos"
df.loc[(df["categoria"].isnull()) & (df["produto"] == "Webcam"), "categoria"] = "Informática"

# removendo as linhas onde a quantidade está vazia porque não temos como saber quantas unidades foram vendidas
df = df.dropna(subset=["quantidade"])

# pegando os produtos que estão com o preço vazio
produtos_sem_preco = df.loc[df["preco_unitario"].isnull(), "produto"].unique()

# verificando quais preços não estão em formato numérico
precos_convertidos = pd.to_numeric(df["preco_unitario"], errors="coerce")

# tirando o R$, os pontos de milhar e trocando a vírgula por ponto
df["preco_unitario"] = (
    df["preco_unitario"]
    .astype(str)
    .str.replace("R$", "", regex=False)
    .str.replace(".", "", regex=False)
    .str.replace(",", ".", regex=False)
    .str.strip()
)

# transformando os preços em número e deixando como vazio o que não conseguir ser convertido
df["preco_unitario"] = pd.to_numeric(df["preco_unitario"], errors="coerce")

# calculando a média do preço de cada produto
media_por_produto = df.groupby("produto")["preco_unitario"].transform("mean")

# preenchendo os preços vazios com a média do mesmo produto
df["preco_unitario"] = df["preco_unitario"].fillna(media_por_produto)

# arredondando os preços para duas casas decimais
df["preco_unitario"] = df["preco_unitario"].round(2)

# tirando espaços extras e deixando as siglas dos estados em maiúsculo
df["estado"] = df["estado"].astype("string").str.strip().str.upper()

# corrigindo os estados que estão escritos por extenso
df["estado"] = df["estado"].replace({
    "SÃO PAULO": "SP",
    "MINAS GERAIS": "MG"
})

# padronizando os estados, tirando espaços extras e deixando as letras em maiúsculo
df["estado"] = df["estado"].astype("string").str.strip().str.upper()

# trocando os estados escritos por extenso pelas suas siglas
df["estado"] = df["estado"].replace({
    "SÃO PAULO": "SP",
    "MINAS GERAIS": "MG"
})

# deixando como vazio os valores que não são siglas de estados válidas
estados_validos = ["SP", "RJ", "MG", "PR", "SC", "RS", "BA", "PE", "GO", "DF"]

df.loc[~df["estado"].isin(estados_validos), "estado"] = pd.NA

# preenchendo os estados vazios ou inválidos porque não temos como descobrir o estado verdadeiro
df["estado"] = df["estado"].fillna("Não informado")

# padronizando as formas de pagamento, tirando espaços extras e deixando as letras em maiúsculo
df["forma_pagamento"] = df["forma_pagamento"].astype("string").str.strip().str.upper()

# padronizando as formas de pagamento, tirando espaços extras e deixando as letras em maiúsculo
df["forma_pagamento"] = df["forma_pagamento"].astype("string").str.strip().str.upper()

# corrigindo as formas de pagamento que estão sem acento
df["forma_pagamento"] = df["forma_pagamento"].replace({
    "CREDITO": "CRÉDITO",
    "DEBITO": "DÉBITO"
})

# definindo quais formas de pagamento são válidas
pagamentos_validos = ["PIX", "CRÉDITO", "DÉBITO", "BOLETO"]

# deixando como vazio tudo que não for uma forma de pagamento válida
df.loc[~df["forma_pagamento"].isin(pagamentos_validos), "forma_pagamento"] = pd.NA

# preenchendo os valores vazios porque não temos como saber a forma de pagamento verdadeira
df["forma_pagamento"] = df["forma_pagamento"].fillna("NÃO INFORMADO")

# padronizando os nomes dos vendedores para deixar todos no mesmo formato
df["vendedor"] = df["vendedor"].astype("string").str.strip().str.title()

# definindo quais vendedores são válidos
vendedores_validos = [
    "Rafael Correia",
    "Leonardo Dias",
    "Fernanda Moraes",
    "Caio Lopes",
    "Juliana Melo",
    "Patrícia Ramos",
    "Gustavo Araújo",
    "Amanda Reis"
]

# deixando como vazio tudo que não for um vendedor válido
df.loc[~df["vendedor"].isin(vendedores_validos), "vendedor"] = pd.NA

# preenchendo os vendedores vazios porque não temos como saber o vendedor verdadeiro
df["vendedor"] = df["vendedor"].fillna("Não informado")

# convertendo as datas para identificar quais valores não estão em um formato válido
datas_convertidas = pd.to_datetime(df["data_venda"], errors="coerce")

# transformando a coluna em data e deixando como vazio os valores que não são datas válidas
df["data_venda"] = pd.to_datetime(df["data_venda"], errors="coerce")

# removendo as linhas onde a data está vazia porque não temos como descobrir a data verdadeira da venda
df = df.dropna(subset=["data_venda"])

# corrigindo as quantidades escritas como texto para transformar tudo em número
df["quantidade"] = df["quantidade"].replace({
    "um": 1,
    "dois": 2,
    "três": 3,
    "quatro": 4,
    "cinco": 5,
    "dez": 10,
    "zero": 0,
    "1 unidade": 1,
    "3 unidades": 3,
    "2x": 2
})

# transformando a coluna quantidade em número e deixando como vazio o que não conseguir ser convertido
df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")

# removendo as linhas onde a quantidade está vazia, igual a zero ou negativa
df = df[df["quantidade"].notnull() & (df["quantidade"] > 0)]

# removendo as linhas que estão completamente duplicadas na base
df = df.drop_duplicates()

# deixando como vazio os preços iguais a zero ou negativos porque são valores inválidos
df.loc[df["preco_unitario"] <= 0, "preco_unitario"] = pd.NA

# calculando novamente a média do preço de cada produto usando apenas os preços válidos
media_por_produto = df.groupby("produto")["preco_unitario"].transform("mean")

# preenchendo os preços inválidos com a média do mesmo produto
df["preco_unitario"] = df["preco_unitario"].fillna(media_por_produto)

# arredondando os preços para duas casas decimais
df["preco_unitario"] = df["preco_unitario"].round(2)

# padronizando as categorias que estão escritas de formas diferentes
df["categoria"] = df["categoria"].replace({
    "Eletrodomesticos": "Eletrodomésticos",
    "casa": "Casa",
    "informática": "Informática",
    "INFORMÁTICA": "Informática",
    "ELETRÔNICOS": "Eletrônicos",
    "eletrônicos": "Eletrônicos",
    "Eletronicos": "Eletrônicos",
    "MOVEIS": "Móveis"
})

# trocando os valores que não representam produtos por "Não informado"
df["produto"] = df["produto"].replace({
    111: "Não informado",
    222: "Não informado",
    333: "Não informado",
    444: "Não informado",
    555: "Não informado"
})

# trocando os números que não representam nomes de clientes por "Não informado"
df["cliente"] = df["cliente"].replace({
    101: "Não informado",
    202: "Não informado",
    303: "Não informado",
    404: "Não informado",
    505: "Não informado"
})

# padronizando os nomes dos clientes, tirando espaços extras e deixando os nomes no mesmo formato
df["cliente"] = df["cliente"].str.strip().str.title()

## transformando a quantidade em número inteiro porque representa unidades vendidas
df["quantidade"] = df["quantidade"].astype(int)

# salvando os dados tratados em uma nova planilha sem alterar o arquivo original
df.to_excel("dados/vendas_tratadas.xlsx", index=False)

# avisando que a nova planilha foi criada
print("Planilha tratada salva com sucesso!")