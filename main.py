import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# empresas
tickers =  ["INTC", "NVDA", "MSFT", "AAPL"]

# periodo
inicio = "2020-01-01"
fim = datetime.today().strftime('%Y-%m-%d')

# baixar dados
dados = yf.download(tickers, start=inicio, end=fim)

# selecionar preco de fechamento
precos = dados["Close"]

# transformar em DataFrame
df = pd.DataFrame(precos)

print(df)

# plotar grafico
plt.figure(figsize=(12,6))

for empresa in df.columns:
    plt.plot(df.index, df[empresa], label=empresa)

plt.title("Evolucao do preco das acoes (2020 - Atual)")
plt.xlabel("Ano")
plt.ylabel("Preco de fechamento (USD)")
plt.legend()
plt.grid(True)

plt.show()
