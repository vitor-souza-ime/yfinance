# Análise de Ações com Python usando yfinance

Este projeto apresenta um exemplo simples de análise de dados do mercado financeiro utilizando Python. O objetivo é coletar dados históricos de ações de grandes empresas de tecnologia e visualizar a evolução de seus preços ao longo do tempo.

O script utiliza a biblioteca `yfinance` para acessar dados do mercado financeiro e gerar um gráfico com os preços de fechamento das ações.

## Empresas analisadas

As empresas analisadas neste exemplo são:

* Intel (INTC)
* NVIDIA (NVDA)
* Microsoft (MSFT)
* Apple (AAPL)

Essas empresas foram escolhidas por serem grandes companhias do setor de tecnologia e semicondutores.

## Período de análise

O período considerado na análise vai de:

2020 até o momento atual.

Isso permite observar tendências recentes do mercado e comparar a evolução do valor das empresas ao longo do tempo.

## Bibliotecas utilizadas

O projeto utiliza as seguintes bibliotecas Python:

* yfinance
* pandas
* matplotlib
* datetime

## Instalação das dependências

Caso as bibliotecas não estejam instaladas, utilize o seguinte comando:

```bash
pip install yfinance pandas matplotlib
```

## Funcionamento do código

O script realiza as seguintes etapas:

1. Define as empresas que serão analisadas através de seus códigos de negociação (tickers).
2. Define o período de coleta dos dados.
3. Utiliza a biblioteca yfinance para baixar os dados históricos das ações.
4. Seleciona o preço de fechamento das ações.
5. Converte os dados para um DataFrame utilizando a biblioteca pandas.
6. Exibe os dados no terminal.
7. Plota um gráfico com a evolução dos preços das ações ao longo do tempo utilizando matplotlib.

## Estrutura do gráfico

O gráfico gerado apresenta:

* eixo X: tempo (anos)
* eixo Y: preço de fechamento das ações em dólares
* uma linha para cada empresa analisada

Isso permite comparar visualmente o desempenho das empresas ao longo do período analisado.

## Possíveis extensões

Este exemplo pode ser expandido para incluir:

* mais empresas
* índices de mercado como S&P 500
* análise de retornos percentuais
* médias móveis
* comparação entre setores econômicos
* aplicações em ciência de dados e aprendizado de máquina

## Objetivo educacional

Este exemplo tem finalidade didática e demonstra como utilizar APIs financeiras para coleta de dados reais e aplicação de técnicas de análise e visualização de dados em Python.
