from flask import Flask, request
import threading
import time

app = Flask(__name__)

class Barbeiro:
    def __init__(self):
        self._lock = threading.Lock()

    def cortarCabelo(self):
        time.sleep(3)

    def cortarBarba(self):
        time.sleep(4)

    def cortarBigode(self):
        time.sleep(5)

    def cortar(self, servico):
        with self._lock:
            if servico == 'cabelo':
                self.cortarCabelo()
            elif servico == 'barba':
                self.cortarBarba()
            elif servico == 'bigode':
                self.cortarBigode()

barbeiro = Barbeiro()

@app.route('/barbeiro/<string:servico>', methods=['POST'])
def cortar(servico):
    barbeiro.cortar(servico)
    return 'Serviço de corte de {} finalizado.'.format(servico)

if __name__ == '__main__':
    app.run(debug=True)
