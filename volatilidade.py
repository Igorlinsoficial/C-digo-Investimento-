#Volatilidade dos ativos comparando-os ao Ibovespa 

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# ativos
ativos = ["PETR4.SA", "ITUB4.SA", 'EGIE3.SA', 'EQTL3.SA', 'BBAS3.SA', 'TIMS3.SA', 'XPLG11.SA', 'ORCL34.SA', 'AAPL34.SA', "^BVSP"]

# dit para armazenar as volatilidades percentuais
volatilidades_percentuais = {}

# pegando dos dados do IBOV
ibov = yf.Ticker("^BVSP")
ibov_data = ibov.history(period="max")
ibov_closing = ibov_data['Close']
ibov_returns = ibov_closing.pct_change().dropna()

# criando loop para calcular a volatilidade % de cada ativo 
for ativo in ativos:
    # Obtenção dos dados do ativo
    data = yf.Ticker(ativo)
    ativo_data = data.history(period="max")
    
    # Verificando dados pra continuar 
    if len(ativo_data) == 0:
        print(f"Dados não disponíveis para {ativo}.")
        continue
    
    # Ajuste de preço
    ativo_closing = ativo_data['Close']
    
    #Cálculo dos retornos logarítmicos
    returns = ativo_closing.pct_change().dropna()
    
    # Cálculo da volatilidade absoluta (desvio padrão) dos retornos
    volatilidade_absoluta = np.std(returns)
    
    # Cálculo da volatilidade em porcentagem
    volatilidade_percentual = volatilidade_absoluta * 100
    
    # Armazenar a volatilidade percentual do ativo no dit
    volatilidades_percentuais[ativo] = volatilidade_percentual
    
    # Exibir a volatilidade percentual de cada ativo no terminal
    print(f"A volatilidade percentual de {ativo} é: {volatilidade_percentual:.4f}%")

# gráfico 
nomes_ativos = list(volatilidades_percentuais.keys())
volatilidades = list(volatilidades_percentuais.values())

# cor (vermelho para o Ibovespa)
cores = ['red' if ativo == "^BVSP" else 'blue' for ativo in nomes_ativos]

plt.bar(nomes_ativos, volatilidades, color=cores)
plt.xlabel('Ativos')
plt.ylabel('Volatilidade em Percentagem')
plt.title('Volatilidade dos Ativos')
plt.xticks(rotation=45)  # Rotacionar os rótulos no eixo x para melhor visualização
plt.show()
