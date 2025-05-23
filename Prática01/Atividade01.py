#Saudação inicial quebra da maldição
print('Olá, Mundo!')

#calculadora de preço total
qnt_products = 10
product = 2

qntd_total = qnt_products * product
print("O preço total é: ", qntd_total)

#calculadora soma
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2

print("A soma de", num1, "e", num2, "é:", soma)

# Calculadora de Volume da Esfera
raio = float(input("Digite o raio da esfera: "))
pi = 3.14
volume_esfera = (4/3) * pi * (raio ** 3)
print("O volume da esfera é:", volume_esfera)

#verifica se a pessoa é maior de idade

maior_idade = int(input("Digite sua idade: "))

if maior_idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")