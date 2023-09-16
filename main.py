from datetime import datetime, timedelta
import pandas as pd
import requests
import script

carrinho1 = "https://images.tcdn.com.br/dev-challenge/cart/4rashtk3sdquptms4md2q2h485.json"
carrinho2 = "https://images.tcdn.com.br/dev-challenge/cart/huni2lib7i0hkbie6vvg7n46t4.json"
carrinho3 = "https://images.tcdn.com.br/dev-challenge/cart/kobq972itl2rqugoa5v2k7e3j7.json"
carrinho4 = "https://images.tcdn.com.br/dev-challenge/cart/qami6pqhjbvgqfh7qqmh4sdud2.json"
carrinho5 = "https://images.tcdn.com.br/dev-challenge/cart/teh1jg167q6k50o2ejermke7u5.json"

response = requests.get(carrinho1)

total = 0
aux = -1
email = ''
for json in response.json():
    total += float(json['Cart']['price'])
    email = json['Cart']['email']
    aux += 1

data = datetime.strptime(
    response.json()[aux]['Cart']['date'], '%Y-%m-%d').date()

data_frete = data + timedelta(15)
data_desconto = data + timedelta(30)

data_inicial = '2023-01-01'
data_final = '2023-12-31'

ano = (pd.date_range(
    start = datetime.strptime(data_inicial, '%Y-%m-%d').date(), 
    end =datetime.strptime(data_final, '%Y-%m-%d').date(), periods = 365))

for d in ano:
    dia = d.date()

    if dia == data_frete:
        print("Você recebeu um cupom de frete gratis para finalização da compra dos itens do carrinho")
        # Método que enviaria o e-mail
        # method.send_email(email)

    if dia == data_desconto:
        if total <= 1000:
            print("Você recebeu um cupom de 10% de desconto para finalização da compra dos itens do carrinho")
            # Método que enviaria o e-mail
            # method.send_email(email)
        else: 
            print("Você recebeu um cupom de 15% de desconto para finalização da compra dos itens do carrinho")
            # Método que enviaria o e-mail
            # method.send_email(email) 

    


