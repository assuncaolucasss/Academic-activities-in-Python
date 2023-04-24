import Pyro4
import os

class Server(object):
    @Pyro4.expose
    def startserver():
        server = Server()
        daemon = Pyro4.Daemon()
        ns = Pyro4.locateNS()
        uri = daemon.register(server)
        ns.register("server", uri)
        print("Ready. Object uri =", uri)
        daemon.requestLoop()

    if __name__ == "__main__":
        startserver()

    register = []
    @Pyro4.expose
    def welcomeMessage(self, name):
        return ('Seja bem vindo,' + str(name))

    @Pyro4.expose
    def upload_file(self, file_name, file_content):
        filepath = os.path.join('dataserver', file_name)
        with open(filepath, 'w' ) as f:
            f.write(file_content)

    @Pyro4.expose
    def list_files(self):
        #Verifica se o diretório possui arquivos
        files = os.listdir('dataserver')
        if len(files) == 0:
            return('Diretório se encontra vazio')
        else:
            return(files)

    @Pyro4.expose
    def download_file(self, file_name):
        # Verificar se o arquivo está disponível
        if file_name in self.register:
            self.register.remove(file_name)
        with open(f'dataserver/{file_name}', 'r') as f:
            file_content = f.read()
        return(file_content)

    @Pyro4.expose
    def register_interest(self, selfregister, state):
        # Adicionar cliente à lista de clientes registrados para o arquivo especificado
       if state == True:
        self.register.append(selfregister)
        return 'Interesse registrado'

    @Pyro4.expose
    def unregister_interest(self, selfregister):
        # Remover cliente da lista de clientes registrados para o arquivo especificado
        if selfregister in selfregister:
            self.register.remove(selfregister)
            return 'Interesse removido'
        return 'Registro não existente'

    @Pyro4.expose
    def get_event(self):
        # Verificar se há eventos para o cliente especificado
        if len (self.register) == 0:
            return ''
        else:
            files = os.listdir('dataserver')
            for f in files:
                if f in self.register:
                    return(f' O arquivo de interesse {f} já está disponível\n')

 