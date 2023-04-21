#Importando as API
from socket import *
import requests
import json

#Menu
op = """
 ____________________
|                    |
| Cotações de Moedas |
|____________________|

--> Escolha umas das opções abaixo:
 _______________________________
|                               |
| [1] - Cotação do Dolar(USD)   |
| [2] - Cotação do Euro(EUR)    |
| [3] - Cotação do Bitcoin(BTC) |
| [0] - Sair                    |
|_______________________________|
"""
#Criando as Váriaveis
cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
cotacoes_dolar = cotacoes['USDBRL']['bid']
cotacoes_euro = cotacoes['EURBRL']['bid']
cotacoes_btc = cotacoes['BTCBRL']['bid']

#Servidor
host = gethostname()
port = 55416
print(f'Conectado no HOST = {host} e na PORTA = {port}')
server = socket(AF_INET, SOCK_STREAM)
server.bind((host,port))
server.listen(5)
con, addr = server.accept()
con.send((op).encode())

#Loop de conexão
while True:
    # Recebe a escolha do cliente
    msg = con.recv(1024).decode()
    if msg == '0':
        con.send("Até a próxima :)".encode())
        break
    elif msg == '1':
        con.send(str(cotacoes_dolar).encode())
    elif msg == '2':
        con.send(str(cotacoes_euro).encode())
    elif msg == '3':
        con.send(str(cotacoes_btc).encode())
    else:
        con.send("Opção inválida. Tente novamente.".encode())





