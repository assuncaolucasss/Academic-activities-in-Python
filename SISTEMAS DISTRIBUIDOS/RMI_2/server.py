import Pyro5.api

class FileServer(object):
    def __init__(self):
        self.file_list = []
        self.registered_clients = {}
        self.event_queue = []

    def upload_file(self, file_name, file_content):
        # Adicionar arquivo à lista de arquivos
        self.file_list.append((file_name, file_content))
        # Verificar se há algum cliente registrado para o arquivo adicionado
        if file_name in self.registered_clients:
            # Adicionar evento de disponibilidade de arquivo à fila de eventos
            for client in self.registered_clients[file_name]:
                self.event_queue.append((client, "O arquivo {} agora está disponível".format(file_name)))

    def list_files(self):
        # Retornar a lista de arquivos
        return [file[0] for file in self.file_list]

    def download_file(self, file_name):
        # Verificar se o arquivo está disponível
        file_content = None
        for file in self.file_list:
            if file[0] == file_name:
                file_content = file[1]
                break
        if file_content is not None:
            return file_content
        else:
            return "Arquivo não encontrado."

    def register_interest(self, client_name, file_name):
        # Adicionar cliente à lista de clientes registrados para o arquivo especificado
        if file_name not in self.registered_clients:
            self.registered_clients[file_name] = []
        self.registered_clients[file_name].append(client_name)

    def unregister_interest(self, client_name, file_name):
        # Remover cliente da lista de clientes registrados para o arquivo especificado
        if file_name in self.registered_clients:
            self.registered_clients[file_name].remove(client_name)

    def get_event(self, client_name):
        # Verificar se há eventos para o cliente especificado
        for event in self.event_queue:
            if event[0] == client_name:
                # Remover evento da fila de eventos e retornar mensagem do evento
                self.event_queue.remove(event)
                return event[1]
        return None

# Registrar o servidor no Pyro
daemon = Pyro5.api.Daemon()
uri = daemon.register(FileServer)

# Iniciar o servidor
print("Servidor iniciado em: ", uri)
daemon.requestLoop()