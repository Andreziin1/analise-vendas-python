# Análise de Vendas com Python

## Sobre o projeto

Este projeto apresenta um processo de análise de dados a partir de uma base de vendas que precisava passar por tratamento antes de ser utilizada

O objetivo foi trabalhar o processo completo: **entender a base recebida, identificar problemas de qualidade, decidir como cada situação deveria ser tratada, validar os dados e, somente depois, iniciar a análise.**

Mais do que obter números, a proposta foi entender o que esses números representam e quais perguntas podem ser respondidas com os dados disponíveis.

---

## Estrutura do projeto

```text
tratamento/
│
├── dados/
│   ├── vendas_brutas_final.xlsx
│   └── vendas_tratadas.xlsx
│
├── dados_vendas.py
├── analise_estatistica.py
└── README.md
```

### `dados_vendas.py`

Responsável pela limpeza, padronização e validação da base original.

### `analise_estatistica.py`

Utiliza a base já tratada para responder às perguntas de negócio e realizar análises estatísticas simples.

### `dados/`

Contém a base original e a versão gerada após o tratamento.

---

## 1. Entendimento e tratamento dos dados

Antes de realizar qualquer análise, comecei conhecendo a estrutura da base e investigando os problemas existentes.

O processo de tratamento seguiu esta lógica:

**Importar → Conhecer → Investigar → Tratar → Validar → Exportar**

A ideia foi evitar alterações automáticas sem antes entender o que estava errado.

Entre os problemas encontrados estavam:

- valores ausentes;
- textos com diferentes padrões de escrita;
- valores inválidos;
- quantidades incorretas;
- preços que precisavam de tratamento;
- datas inválidas;
- registros duplicados;
- informações categóricas sem padronização.

### Decisões tomadas durante o tratamento

Nem todo dado incorreto foi simplesmente excluído.

Quando uma informação podia ser recuperada com segurança, ela foi corrigida. Por exemplo, valores de quantidade escritos como texto, mas com significado claro, puderam ser convertidos para números.

Quando não existia informação suficiente para descobrir o valor correto, preferi **não inventar o dado**.

Campos não essenciais, como estado ou vendedor, puderam ser mantidos como **"Não informado"** quando não havia uma correção confiável.

Já registros com problemas em informações essenciais para a análise, quando não podiam ser recuperados de forma segura, foram removidos.

Para preços ausentes ou inválidos, utilizei como referência a **média do mesmo produto**. A escolha foi usar informações do próprio grupo do produto em vez de aplicar uma média geral a itens com características e preços diferentes.

Também foram removidos registros exatamente duplicados e os IDs de venda foram verificados para garantir que não existissem identificadores repetidos na base final.

### Resultado do tratamento

A base final ficou com:

- **942 registros**
- **10 colunas**
- **0 valores nulos**
- **0 registros exatamente duplicados**
- **0 IDs de venda duplicados**

A base tratada foi então exportada para `dados/vendas_tratadas.xlsx`, separando a etapa de preparação da etapa de análise.

---

## 2. Análise dos dados

Com a base tratada, foi criada a variável de faturamento:

```python
df["faturamento"] = df["quantidade"] * df["preco_unitario"]
```

Esse cálculo permite analisar a receita gerada por cada venda utilizando informações que já existiam na base.

A partir disso, procurei responder perguntas como:

1. Quanto a empresa faturou no total?
2. Quais produtos e categorias geraram mais faturamento?
3. Quais produtos venderam mais unidades?
4. Qual vendedor realizou mais vendas e qual gerou mais faturamento?
5. Qual estado teve mais vendas e qual gerou mais faturamento?
6. Como as formas de pagamento estão distribuídas?
7. Qual o ticket médio de cada cliente?
8. Quantas compras cada cliente realizou?
9. Qual porcentagem dos clientes comprou mais de uma vez?
10. Qual o ticket médio geral das vendas?
11. Como o faturamento se comportou ao longo dos meses?
12. Existe relação entre quantidade vendida e faturamento?
13. Quais produtos apresentam maior quantidade média por venda?
14. Quais clientes representam a maior parte do faturamento?
15. Sabendo que uma venda é de Eletrônicos, qual a probabilidade de ela ter sido paga via PIX?

---

## 3. Principais resultados

O faturamento total registrado na base foi de aproximadamente **R$ 217,3 milhões**.

### Faturamento não é a mesma coisa que volume de vendas

O **Notebook** apresentou o maior faturamento, com aproximadamente **R$ 79,9 milhões**, embora não tenha sido o produto com maior número de unidades vendidas.

O **Teclado**, por outro lado, liderou em quantidade, com **267 unidades**, enquanto o Notebook teve **253 unidades vendidas**.

Esse resultado mostra por que analisar somente quantidade vendida pode produzir uma visão incompleta do desempenho de um produto.

### Eletrônicos concentram grande parte da receita

A categoria **Eletrônicos** apresentou aproximadamente **R$ 151,1 milhões em faturamento**, representando cerca de **69,5% do faturamento total da base**.

Isso mostra uma concentração relevante da receita nessa categoria.

Ainda assim, maior faturamento não significa necessariamente maior lucro, pois a base não possui informações sobre custos ou margens.

### Vendedores

**Rafael Correia** apresentou a maior quantidade de vendas, com **137 registros**, e também o maior faturamento, com aproximadamente **R$ 33,9 milhões**.

Ao comparar os demais vendedores, quantidade de vendas e faturamento não seguem exatamente a mesma ordem. Isso abre espaço para uma análise complementar de ticket médio por vendedor.

### Mais vendas não significam necessariamente maior faturamento

Entre os estados, **Pernambuco (PE)** apresentou a maior quantidade de vendas, com **105 registros**.

Porém, o maior faturamento foi registrado em **Goiás (GO)**, com aproximadamente **R$ 26,8 milhões**.

O resultado reforça que volume de vendas e faturamento são métricas diferentes e precisam ser analisadas em conjunto.

### Formas de pagamento

As formas de pagamento apresentaram uma distribuição relativamente equilibrada:

- Crédito: **27,39%**
- Boleto: **24,20%**
- Débito: **23,89%**
- PIX: **22,93%**
- Não informado: **1,59%**

Não houve uma única forma de pagamento concentrando a maior parte das vendas.

### Comportamento dos clientes

**Carla Mendes** apresentou a maior frequência, com **56 compras**.

Já **Isabela Santos**, mesmo com menos compras (**44**), apresentou o maior faturamento entre os clientes identificados, com aproximadamente **R$ 15,9 milhões**, além do maior ticket médio.

Isso reforça a diferença entre analisar **frequência de compra** e **valor gerado**.

### Recorrência

Entre os clientes identificados, **100% realizaram mais de uma compra**.

Apesar de o cálculo estar correto para a base, esse resultado precisa ser interpretado com cautela. Existem poucos nomes de clientes distribuídos entre centenas de registros e a base não possui um identificador único de cliente.

Por isso, essa métrica descreve os dados disponíveis, mas não deve ser tratada como uma medida definitiva de retenção.

### Ticket médio

O ticket médio geral das vendas foi de aproximadamente **R$ 230,7 mil**.

Como a média pode ser influenciada por vendas de valores elevados, uma análise futura pode comparar esse resultado com a mediana para entender melhor a distribuição dos valores das vendas.

### Análise ao longo do tempo

No período registrado na base, **janeiro** apresentou o maior faturamento mensal, com aproximadamente **R$ 32,5 milhões**, enquanto **agosto** apresentou o menor, com aproximadamente **R$ 21,3 milhões**.

Esses valores descrevem o comportamento observado nos dados disponíveis. Como a base não informa explicitamente se todos os dias de cada mês possuem cobertura completa, a comparação mensal deve ser interpretada considerando essa limitação.

---

## 4. Estatística e probabilidade

Além das análises descritivas, utilizei alguns conceitos básicos de estatística.

### Correlação

A correlação entre quantidade vendida e faturamento foi de aproximadamente **0,31**.

O resultado indica uma associação linear positiva, porém não forte, entre as duas variáveis.

Como o faturamento é calculado a partir da quantidade multiplicada pelo preço unitário, parte dessa relação já existe pela própria forma como a variável foi construída. O preço dos produtos também influencia diretamente o resultado.

Além disso, correlação indica associação e não deve ser interpretada, por si só, como relação de causa e efeito.

### Probabilidade condicional

Também foi analisada a seguinte pergunta:

**Sabendo que uma venda pertence à categoria Eletrônicos, qual a probabilidade de ela ter sido paga via PIX?**

O resultado encontrado foi de aproximadamente **24,23%**.

Nesse caso, a análise considera somente as vendas de Eletrônicos e verifica, dentro desse grupo, a proporção realizada via PIX.

Esse exemplo aplica de forma simples o conceito de probabilidade condicional aos dados do projeto.

---

## 5. Limitações da análise

A base permite analisar vendas e faturamento, mas não possui informações sobre:

- custo dos produtos;
- margem de lucro;
- despesas;
- estoque;
- investimento realizado.

Por esse motivo, **maior faturamento não significa necessariamente maior lucro ou melhor retorno sobre investimento**.

Os resultados permitem identificar onde a receita está concentrada, mas não são suficientes, sozinhos, para decidir onde a empresa deveria investir mais ou menos.

Também existem registros classificados como **"Não informado"**. Eles foram mantidos quando não havia informação suficiente para realizar uma correção segura e quando excluir toda a venda significaria perder outras informações válidas.

Na análise de clientes, nomes iguais foram considerados como pertencentes ao mesmo cliente. Como a base não possui um identificador único de cliente, a análise de recorrência deve ser entendida como uma aproximação.

Essas limitações são importantes para evitar conclusões que os dados disponíveis não conseguem sustentar.

---

## 6. Tecnologias utilizadas

- **Python**
- **Pandas**
- **Excel**
- **VS Code**

---

## Conclusão

A análise mostrou que olhar apenas para volume de vendas não é suficiente para entender o desempenho da operação.

O produto com mais unidades vendidas não foi o que mais faturou, o estado com mais vendas não apresentou o maior faturamento e o cliente com maior frequência de compras não foi o que gerou a maior receita.

O tratamento da base teve impacto direto na confiabilidade desses resultados. Por isso, valores só foram corrigidos quando existia informação suficiente para sustentar a alteração; nos demais casos, foram mantidos como não informados ou removidos quando comprometiam a análise.

Com os dados disponíveis foi possível analisar receita, comportamento de compra e alguns padrões de vendas. Já decisões relacionadas a lucro ou retorno sobre investimento exigiriam informações adicionais, principalmente custos e margens.
