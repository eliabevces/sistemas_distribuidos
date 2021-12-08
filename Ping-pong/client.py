import socket                          
from time import sleep

sock = socket.socket()          

host = socket.gethostname()    

port = 11111  

print("Conectando-se ao servidor")

sock.connect((host, port))

print("Conectado.")


while 1:

   print("Digite mensagem:")

   x = input()

   if x == 'SAIR':
        print('Desconectando.')
        sock.send(x.encode())
        sock.close()
        break

   sock.send(x.encode())

   print("Mensagem enviada")
   print('Esperando resposta')

   data = sock.recv(1024)

   if data.decode() == 'SAIR':
        print('Conexão encerrada.')
        sock.close()
        break
    
   print('Resposta recebida:')
   
   print(data.decode())