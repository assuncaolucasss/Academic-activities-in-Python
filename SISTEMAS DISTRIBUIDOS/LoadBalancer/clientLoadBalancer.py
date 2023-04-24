import Pyro4
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit


# Classe da interface gráfica de usuário
class LoadBalancerInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.load_balancer = Pyro4.Proxy("PYRONAME:load_balancer")
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Load Balancer')
        self.setGeometry(100, 100, 400, 300)

        # Elementos da interface
        self.label = QLabel('Servidor:', self)
        self.server_input = QLineEdit(self)
        self.server_input.setPlaceholderText('Digite o nome do servidor')
        self.add_server_button = QPushButton('Adicionar Servidor', self)
        self.remove_server_button = QPushButton('Remover Servidor', self)
        self.balance_load_button = QPushButton('Balancear Carga', self)
        self.show_servers_button = QPushButton('Mostrar Servidores', self)
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)

        # Layout da interface
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.server_input)
        layout.addWidget(self.add_server_button)
        layout.addWidget(self.remove_server_button)
        layout.addWidget(self.balance_load_button)
        layout.addWidget(self.show_servers_button)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

        # Conectar os botões aos métodos correspondentes
        self.add_server_button.clicked.connect(self.add_server)
        self.remove_server_button.clicked.connect(self.remove_server_button)
        self.balance_load_button.clicked.connect(self.balance_load_button)
        self.show_servers_button.clicked.connect(self.show_servers_button)

    def remove_server(self):
        server_name = self.server_input.text()
        result = self.load_balancer.remove_server(server_name)
        self.result_text.append(result)

    def balance_load(self):
        result = self.load_balancer.balance_load()
        self.result_text.append(result)

    def show_servers(self):
        servers = self.load_balancer.show_servers()
        result = f'Servidores disponíveis: {", ".join(servers)}'
        self.result_text.append(result)

    def add_server(self):
        server_name = self.server_input.text()
        result = self.load_balancer.add_server(server_name)
        self.result_text.append(result)

if __name__ == '__main__':
    app = QApplication([])
    window = LoadBalancerInterface()
    window.show()
    app.exec_()

