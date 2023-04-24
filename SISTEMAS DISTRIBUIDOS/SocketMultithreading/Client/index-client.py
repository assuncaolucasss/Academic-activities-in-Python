import threading
import socket

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nNão foi possível realizar uma conexão com o servidor')

    username = input('\tInsira o nome de usuário: ')
    print('\n\tConectado')
    
    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()

    def receiveMessages(client):
        while True:
            try:
                msg = client.recv(2048).decode('utf-8')
                print(msg + ('\n') )
            except:
                print('\n\tNão foi possível permanecer conectado ao servidor!\n')
                print('Pressione <Enter> para continuar...')
                client.close()
                break
                
    def sendMessages(client):
        while True:
            try:
                msg = input('\n')
                client.send('<{username}> {msg}'.encode('utf-8'))
            except:
                return




    main()