#importando as bibliotecas necessárias
import requests, smtplib, ssl
from email.message import EmailMessage

#pegando o carrinho desejado e atribuindo a uma variável
cart1 = "https://images.tcdn.com.br/dev-challenge/cart/4rashtk3sdquptms4md2q2h485.json"
response = requests.get(cart1)
#colocando o(s) produto(s) em uma variável p
for products in response.json():
    p = products['Cart']['product_name']

total = 0
aux = -1
for json in response.json():
    total += float(json['Cart']['price'])
    aux += 1

#criando uma função para enviar o email
def send_email(receiver): 
    sender= 'email@mail.com' #definindo o email de onde será enviado
    password= 'senha12345' #definindo uma senha para fazer login
    subject= "Compra não finalizada!" #essa é a parte do email "Assunto"
    #definindo um corpo para o email, ou seja, a mensagem que será enviada
    if total <= 1000:
        body= "Você não finalizou a compra dos produtos: ", p, "estamos dando um cupom de 10% desconto na finalização da compra dos produtos do carrinho, mas CORRA, esse cupom é por tempo LIMITADO!!"
    else:
        body= "Você não finalizou a compra dos produtos: ", p, "estamos dando um cupom de 15% desconto na finalização da compra dos produtos do carrinho, mas CORRA, esse cupom é por tempo LIMITADO!!"
    em = EmailMessage() #atribuindo a função 'EmailMessage' da biblioteca com o mesmo nome para uma variável em
    em['From'] = sender #atribuindo o emissor 'From' pela função que criamos anteriormente 
    em['to'] = receiver #o mesmo para o receptor, mas dessa vez com 'to'
    em['Subject'] = subject #atribuindo o assunto do email com a variável 'subject'
    em.set_content(body) #definindo a mensagem do email 

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender,password)
        smtp.sendmail(sender, receiver, em.as_string())



