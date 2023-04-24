import Pyro4
import random


# Classe que representa um servidor
class Server:
    def __init__(self, name):
        self.name = name

    def process_request(self):
        """Simula o processamento de uma solicitação."""
        return f'Servidor {self.name}: Solicitação processada.'


# Classe do sistema de balanceamento de carga
class LoadBalancer:
    def __init__(self):
        self.servers = []

    def add_server(self, server):
        """Adiciona um servidor à DHT."""
        self.servers.append(server)
        return f'Servidor {server.name} adicionado com sucesso.'

    def remove_server(self, server_name):
        """Remove um servidor da DHT."""
        server = next((s for s in self.servers if s.name == server_name), None)
        if server:
            self.servers.remove(server)
            return f'Servidor {server_name} removido com sucesso.'
        else:
            return f'Servidor {server_name} não encontrado na DHT.'

    def balance_load(self):
        """Executa o balanceamento de carga usando o algoritmo Round Robin."""
        if not self.servers:
            return 'Nenhum servidor disponível para balanceamento de carga.'

        server = random.choice(self.servers)  # Seleciona um servidor aleatório
        return f'Servidor {server.name} selecionado para balanceamento de carga.'

    def show_servers(self):
        """Retorna a lista de servidores atual."""
        return [server.name for server in self.servers]


# Iniciar o servidor Pyro4
def start_server():
    lb = LoadBalancer()
    daemon = Pyro4.Daemon()
    uri = daemon.register(lb)
    ns = Pyro4.locateNS()
    ns.register('load_balancer', uri)
    print('Servidor iniciado.')
    daemon.requestLoop()


if __name__ == '__main__':
    start_server()
