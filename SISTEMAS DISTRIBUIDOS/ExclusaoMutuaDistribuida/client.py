import requests
import threading

class Cliente:
    def __init__(self, url):
        self._url = url

    def cortarCabelo(self):
        requests.post(self._url + '/cabelo')

    def cortarBarba(self):
        requests.post(self._url + '/barba')

    def cortarBigode(self):
        requests.post(self._url + '/bigode')

    def competir(self):
        for i in range(20):
            self.cortarCabelo()
            self.cortarBarba()
            self.cortarBigode()

barbeiro_url = 'http://localhost:5000/barbeiro'
clientes = []
for i in range(5):
    cliente = Cliente(barbeiro_url)
    clientes.append(cliente)

threads = []
for cliente in clientes:
    thread = threading.Thread(target=cliente.competir)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
on.close()
