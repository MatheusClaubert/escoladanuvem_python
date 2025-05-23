# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15

# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
# Resposta:
#
valorReais = 100.00
taxaDolar = 5.20
taxaEuro = 6.15
valorDolar = valorReais / taxaDolar
valorEuro = valorReais / taxaEuro

print("Conversão de Moeda")   
print(f"Valor em Reais: R$ {valorReais:.2f}")
print(f"Valor em Dólares: $ {valorDolar:.2f}")
print(f"Valor em Euros: € {valorEuro:.2f}")

# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

# Resposta:
produto = "Camiseta"
precoOriginal = 50.00
porcentagemDesconto = 20
desconto = (precoOriginal * porcentagemDesconto) / 100  
precoFinal = precoOriginal - desconto
print("\nCalculadora de Desconto")
print(f"Produto: {produto}")
print(f"Preço Original: R$ {precoOriginal:.2f}")
print(f"Porcentagem de Desconto: {porcentagemDesconto}%")
print(f"Valor do Desconto: R$ {desconto:.2f}")
print(f"Preço Final: R$ {precoFinal:.2f}")

# 3- Calculadora de Média Escolar
# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

# * Nota 1: 7.5
# * Nota 2: 8.0
# * Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
# Resposta:
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
media = (nota1 + nota2 + nota3) / 3
print("\nCalculadora de Média Escolar")
print(f"nota 1: {nota1:.2f}\n nota 2: {nota2:.2f}\n nota 3: {nota3:.2f}\n")
print(f"Média: {media:.2f}")

# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
# Resposta:
distanciaPercorrida = 300
combustivelGasto = 25
consumoMedio = distanciaPercorrida / combustivelGasto
print("\nCalculadora de Consumo de Combustível")
print(f"Distância Percorrida: {distanciaPercorrida} km")
print(f"Combustível Gasto: {combustivelGasto} litros")
print(f"Consumo Médio: {consumoMedio:.2f} km/l")