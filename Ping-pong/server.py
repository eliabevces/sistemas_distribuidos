import socket                               
from time import sleep

sock = socket.socket()           

host = socket.gethostname()    

port = 11111           

sock.bind((host, port))

print('Esperando conexao')

sock.listen()        

c, addr = sock.accept()

print('Conectado')

while 1:

   print('Esperando mensagem')

   data = c.recv(1024)

   if data.decode() == 'SAIR':
        print('Conexão encerrada.')
        print('Esperando conexao')

        sock.listen()          

        c, addr = sock.accept()

        print('Conectado')
   else:     
       print('Mensagem recebida:')
       print(data.decode())
       print('Digite resposta:')

       x = input()

       if x == 'SAIR':
            print('Desconectando.')
            c.sendall(x.encode())
            sock.close() 
            break
        
       c.sendall(x.encode())