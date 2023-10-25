#CÓDIGO QUE COMPARA A CARTEIRA COM O IBOV NOS DOIS ÚLTIMOS ANOS 
#obs: necessário instalar bibliotecas! Se estiver no VS code, use o myenv. 

import yfinance as yf
import matplotlib.pyplot as plt
import datetime

ativos = ["PETR4.SA", "ITUB4.SA", 'EGIE3.SA', 'EQTL3.SA', 'BBAS3.SA', 'TIMS3.SA', 'XPLG11.SA', 'ORCL34.SA', 'AAPL34.SA']

# Data de início e fim para os últimos dois anos
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=730)  # Retrocede 730 dias a partir da data atual

#dados históricos dos ativos
data = yf.download(ativos, start=start_date, end=end_date)['Adj Close']

# calcula os retornos diários
returns = data.pct_change()

# calcula a média dos retornos diários de seus ativos
average_portfolio_return = returns.mean(axis=1)

# baixa os dados históricos do IBOV
ibov = yf.download("^BVSP", start=start_date, end=end_date)['Close']

# calcula o retorno diário do IBOV
ibov_return = ibov.pct_change()

# Plote os retornos para comparação
plt.figure(figsize=(12, 6))
plt.plot(average_portfolio_return.cumsum() * 100, label='Carteira Média')
plt.plot(ibov_return.cumsum() * 100, label='IBOV')
plt.title('Desempenho da Carteira Média vs. IBOV (Últimos 2 Anos)')
plt.xlabel('Data')
plt.ylabel('Retorno Acumulado (%)')
plt.legend()
plt.grid()
plt.show()
