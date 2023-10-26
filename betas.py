import yfinance as yf
import statsmodels.api as sm


ativos = ["PETR4.SA", "ITUB4.SA", 'EQTL3.SA', 'BBAS3.SA', 'TIMS3.SA', 'XPLG11.SA', 'ORCL34.SA', 'AAPL34.SA', "^BVSP"]

# Dit 
betas = {}

#  dados do IBOV
ibov = yf.Ticker("^BVSP")
ibov_data = ibov.history(period="max")
ibov_closing = ibov_data['Close']
ibov_returns = ibov_closing.pct_change().dropna()

# Loop para calcular o Beta de cada ativo
for ativo in ativos:
    # dados do ativo
    data = yf.Ticker(ativo)
    ativo_data = data.history(period="max")
    ativo_closing = ativo_data['Close']
    ativo_returns = ativo_closing.pct_change().dropna()
    
    # Alinhe as séries temporais pelos índices
    aligned_returns = ativo_returns.reindex(ibov_returns.index)
    
    # Cálculo do Beta com as séries temporais alinhadas
    X = sm.add_constant(ibov_returns)
    model = sm.OLS(aligned_returns, X, missing='drop').fit()
    ativo_beta = model.params[1]
    
    # Armazene o Beta do ativo no dicionário
    betas[ativo] = ativo_beta

# Exiba os Betas calculados para cada ativo
for ativo, beta in betas.items():
    print(f"O Beta de {ativo} em relação ao IBOV é:", round(beta, 2))
