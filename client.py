#Importação
from socket import *
#Cliente
host = gethostname()
port = 55416
client = socket(AF_INET, SOCK_STREAM)
client.connect((host,port))
#Recebe o Menu
menu = client.recv(1024)
print(menu.decode())
#Loop de conexão
while 1:
    #Cliente faz escolha da cotação
    msg = int(input('Qual cotação deseja saber? '))
    #Envia a escolha para o servidor
    client.send(str(msg).encode())
    #Classe de moedas
    moedas = {1:'Dólar', 2:'Euro', 3:'Bitcoin'}
    #Encerra a conexão
    if msg == 0:
        print('\nAté a próxima :)')
        client.close
        break
    #Recebe a cotação escolhida
    elif (msg) > 0 and (msg) < 4:
        print(f'\nA cotação atual do {moedas[msg]} é R${client.recv(1024).decode()}\n')
    else:
        print('Opção inválida. Tente novamente.')
