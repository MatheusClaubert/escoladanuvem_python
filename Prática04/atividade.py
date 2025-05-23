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
