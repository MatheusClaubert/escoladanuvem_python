notas = []
while True:
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim': 
        break 
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim' para encerrar.")
if notas:
    media = sum(notas) / len(notas)
    print(f"Média das notas: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")


#Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). 
# Se o resultado é True, responda “Sim”, se o resultado for False, responda "Não"
def eh_palindromo(texto):
        inverso = texto[::-1]
        if inverso == texto:
            return True
        else:
            return False
        


#Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
def idade_em_dias(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade * 365  # Considerando 365 dias por ano
