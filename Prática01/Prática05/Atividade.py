# Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL).
# O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP),
# e o programa deve exibir o valor atual, máximo e mínimo da cotação, 
# além da data e hora da última atualização.
# Utilize a API da AwesomeAPI para obter os dados de cotação
import requests
def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        if moeda in dados:
            cotacao = dados[moeda]
            print(f"Cotação atual de {moeda}: R$ {cotacao['bid']}")
            print(f"Valor máximo: R$ {cotacao['high']}")
            print(f"Valor mínimo: R$ {cotacao['low']}")
            print(f"Data e hora da última atualização: {cotacao['create_date']}")
        else:
            print("Moeda não encontrada.")
    else:
        print("Erro ao consultar a API.")