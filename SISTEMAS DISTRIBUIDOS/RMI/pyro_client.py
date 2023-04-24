import Pyro4
import os

def main():
    name = input('Insira seu nome: ').strip()
    server = Pyro4.Proxy('PYRONAME:server')
    print(server.welcomeMessage(name))

    print('''\n\t\tMENU:
        \t1. Fazer upload de arquivo
        \t2. Consultar arquivos disponíveis
        \t3. Fazer download de arquivo
        \t4. Registrar interesse em arquivo
        \t5. Cancelar registro de interesse
        \t6. Sair
    ''')

# Loop do cliente para receber comandos
while True:
        command = input('\tEscolha uma opção\n>>>>>').strip().upper()
        if command == '1':
            path = input('Qual o caminho do arquivo?')
            with open(f'{path}', 'r') as f:
                text = f.read()
            filename = path.split('/')[-1]
            server.uploadFile(filename, text)
            print('Arquivo enviado!')

        if command == '2':
            print(server.listFiles())

        if command == '3':
            filename = input('Qual o nome do arquivo?')
            text = server.downloadFile(filename)
            filepath = os.path.join('dataclient', filename)
            with open(filepath, 'w') as f:
                f.write(text)
            print('O download do arquivo foi concluído!')

        if command == '4':
            filename = input('Qual o nome do arquivo que deseja ser notficado?')
            print(server.register_interest(filename, True))

        if command == '5':
            filename = input('Qual o nome do arquivo que deseja parar de ser notificado?')
            print(server.unregister_interest(filename, False))

        if command == '6':
            print('Sessão finalizada!')
            break

        print(server.registerNotification(), end='')

if __name__ == '__main__':
    main()