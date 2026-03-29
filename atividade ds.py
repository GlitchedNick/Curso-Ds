#Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em watts): "))
horas = float(input("Digite o número de horas que o aparelho é utilizado por dia: "))
# Cálculo do consumo diário em kWh
consumo_diario = (potencia * horas) / 1000
# Cálculo do consumo mensal
consumo_mensal = consumo_diario * 30
# Cálculo do custo mensal (considerando o preço de R$ 0,75)
preco_kwh = 0.75
custo_mensal = consumo_mensal * preco_kwh
# Saída dos resultados
print(f"Consumo diário de {aparelho}: {consumo_diario:.2f} kWh")
print(f"Consumo mensal de {aparelho}: {consumo_mensal:.2f} kWh")
print(f"Custo mensal de {aparelho}: R$ {custo_mensal:.2f}")