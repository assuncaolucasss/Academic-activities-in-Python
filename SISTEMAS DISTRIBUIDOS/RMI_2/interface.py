import PySimpleGUI as sg
from fileclient import FileClient

def download_file(file_name, client):
    # Verifica se o arquivo existe no servidor
    if file_name not in client.get_files():
        sg.Popup(f'Arquivo {file_name} não existe no servidor')
        return

    # Baixa o arquivo do servidor
    content = client.download_file(file_name)

    # Salva o arquivo localmente
    with open(file_name, 'wb') as f:
        f.write(content)
    
    sg.Popup(f'Download completo: {file_name}')

def upload_file(file_path, client):
    # Carrega o arquivo para o servidor
    with open(file_path, 'rb') as f:
        client.upload_file(file_path, f.read())

    sg.Popup(f'Upload completo: {file_path}')

def register_interest(file_name, client):
    # Registrar interesse pelo arquivo
    client.register_interest(file_name)

    sg.Popup(f'Interesse registrado para o arquivo: {file_name}')

def unregister_interest(file_name, client):
    # Cancelar o registro de interesse para o arquivos
    client.unregister_interest(file_name)

    sg.Popup(f'Cancelamento de registro de interesse para o arquivo: {file_name}')

def create_gui():
    # Cria a interface
    layout = [
        [sg.Text('Nome do arquivo'), sg.Input(key='file_name')],
        [sg.Button('Download'), sg.Button('Registrar interesse'), sg.Button('Cancelar registro de interesse')],
        [sg.Text('Caminho do arquivo'), sg.Input(key='file_path'), sg.FileBrowse()],
        [sg.Button('Upload')],
        [sg.Output(size=(60, 10))]
    ]

    # Cria janela
    window = sg.Window('RMI', layout)


    # Conecta ao Pyro server
    client = FileClient()

    # Loop de eventos
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Download':
            download_file(values['file_name'], client)

        if event == 'Upload':
            upload_file(values['file_path'], client)

        if event == 'Registrar interesse':
            register_interest(values['file_name'], client)

        if event == 'Cancelar registro de interesse':
            unregister_interest(values['file_name'], client)

    # Desconecta Pyro server
    client.disconnect()
    
    # Fecha
    window.close()

if __name__ == '__main__':
    create_gui()