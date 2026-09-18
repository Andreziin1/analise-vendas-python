import pandas as pd

# importando a base tratada
df = pd.read_excel("dados/vendas_tratadas.xlsx")

# criando o faturamento de cada venda
df["faturamento"] = df["quantidade"] * df["preco_unitario"]


# 1. Quanto a empresa faturou no total?
print(f"Faturamento total: R$ {df['faturamento'].sum():,.2f}")


# 2. Quais produtos e categorias geraram mais faturamento?
print("\nFaturamento por produto:")
print(
    df.groupby("produto")["faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\nFaturamento por categoria:")
print(
    df.groupby("categoria")["faturamento"]
    .sum()
    .sort_values(ascending=False)
)


# 3. Quais produtos venderam mais unidades?
print("\nUnidades vendidas por produto:")
print(
    df.groupby("produto")["quantidade"]
    .sum()
    .sort_values(ascending=False)
)


# 4. Qual vendedor realizou mais vendas e qual gerou mais faturamento?
print("\nQuantidade de vendas por vendedor:")
print(
    df.groupby("vendedor")["id_venda"]
    .count()
    .sort_values(ascending=False)
)

print("\nFaturamento por vendedor:")
print(
    df.groupby("vendedor")["faturamento"]
    .sum()
    .sort_values(ascending=False)
)


# 5. Qual estado teve mais vendas e qual gerou mais faturamento?
print("\nQuantidade de vendas por estado:")
print(
    df.groupby("estado")["id_venda"]
    .count()
    .sort_values(ascending=False)
)

print("\nFaturamento por estado:")
print(
    df.groupby("estado")["faturamento"]
    .sum()
    .sort_values(ascending=False)
)


# 6. Qual a porcentagem de cada forma de pagamento?
print("\nPorcentagem por forma de pagamento:")
print(
    (df["forma_pagamento"].value_counts(normalize=True) * 100)
    .round(2)
)


# 7. Qual o ticket médio de cada cliente?
print("\nTicket médio por cliente:")
print(
    df.groupby("cliente")["faturamento"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)


# 8. Quantas compras cada cliente realizou?
print("\nQuantidade de compras por cliente:")
print(
    df.groupby("cliente")["id_venda"]
    .count()
    .sort_values(ascending=False)
)


# 9. Qual porcentagem dos clientes comprou mais de uma vez?
clientes = df[df["cliente"] != "Não Informado"]
compras_clientes = clientes.groupby("cliente")["id_venda"].count()

print(
    f"\nClientes que compraram mais de uma vez: "
    f"{((compras_clientes > 1).sum() / compras_clientes.count()) * 100:.2f}%"
)


# 10. Qual é o ticket médio geral das vendas?
print(f"\nTicket médio geral: R$ {df['faturamento'].mean():,.2f}")


# 11. Como o faturamento se comporta ao longo do tempo?
print("\nFaturamento por mês:")
print(
    df.groupby(df["data_venda"].dt.to_period("M"))["faturamento"]
    .sum()
)


# 12. Existe relação entre quantidade vendida e faturamento?
print(
    f"\nCorrelação entre quantidade e faturamento: "
    f"{df['quantidade'].corr(df['faturamento']):.2f}"
)


# 13. Quais produtos costumam ser comprados em maior quantidade por venda?
print("\nQuantidade média por venda de cada produto:")
print(
    df.groupby("produto")["quantidade"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)


# 14. Quais clientes representam a maior parte do faturamento?
print("\nFaturamento por cliente:")
print(
    df.groupby("cliente")["faturamento"]
    .sum()
    .sort_values(ascending=False)
)


# 15. Sabendo que uma venda é de Eletrônicos, qual a probabilidade de ela ter sido paga por PIX?
eletronicos = df[df["categoria"] == "Eletrônicos"]

print(
    f"\nProbabilidade de uma venda de Eletrônicos ser paga por PIX: "
    f"{((eletronicos['forma_pagamento'] == 'PIX').sum() / len(eletronicos)) * 100:.2f}%"
)
