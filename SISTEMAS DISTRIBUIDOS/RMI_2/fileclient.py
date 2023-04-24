import Pyro5.api

# Define a URI para se conectar ao servidor
SERVER_URI = "PYRO:file_server@localhost:9090"

# Conecta ao servidor
file_server = Pyro5.api.Proxy(SERVER_URI)

# Loop do cliente para receber comandos
while True:
    print("MENU:")
    print("1. Fazer upload de arquivo")
    print("2. Consultar arquivos disponíveis")
    print("3. Fazer download de arquivo")
    print("4. Registrar interesse em arquivo")
    print("5. Cancelar registro de interesse")
    print("0. Sair")
    choice = input("Digite a opção desejada: ")

    if choice == "1":
        file_name = input("Digite o nome do arquivo a ser enviado: ")
        file_contents = input("Digite o conteúdo do arquivo a ser enviado: ")
        result = file_server.upload_file(file_name, file_contents)
        print(result)

    elif choice == "2":
        file_list = file_server.list_files()
        print("Arquivos disponíveis:")
        for file_name in file_list:
            print(file_name)

    elif choice == "3":
        file_name = input("Digite o nome do arquivo a ser baixado: ")
        file_contents = file_server.download_file(file_name)
        print(file_contents)

    elif choice == "4":
        file_name = input("Digite o nome do arquivo para se registrar interesse: ")
        client_uri = Pyro5.api.current_context.client_sock_addr
        result = file_server.register_interest(file_name, client_uri)
        print(result)

    elif choice == "5":
        file_name = input("Digite o nome do arquivo para cancelar registro de interesse: ")
        client_uri = Pyro5.api.current_context.client_sock_addr
        result = file_server.cancel_interest(file_name, client_uri)
        print(result)

    elif choice == "0":
        break

    else:
        print("Opção inválida")