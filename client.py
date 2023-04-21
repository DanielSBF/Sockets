from socket import *

host = gethostname()
port = 55416

client = socket(AF_INET, SOCK_STREAM)
client.connect((host,port))
msg2 = client.recv(1024)
print(msg2.decode())
while 1:
    msg = input('Qual cotação deseja saber? ')
    client.send(msg.encode())
    if msg == '0':
        print()
        print('Até a próxima :)')
        client.close
        break
    elif msg == '1':
        dolar = client.recv(1024).decode()
        print()
        print(f'A cotação atual do Dólar é R${dolar}')
        print()
    elif msg == '2':
        euro = client.recv(1024).decode()
        print()
        print(f'A cotação atual do Euro é R${euro}')
        print()
    elif msg == '3':
        btc = client.recv(1024).decode()
        print()
        print(f'A cotação atual do Bitcoin é R${btc}')
        print()
    else:
        invalido = client.recv(1024).decode()
        print()
        print('Opção inválida. Tente novamente.')
        print()
    
    