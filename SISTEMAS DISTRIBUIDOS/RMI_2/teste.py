import PySimpleGUI as sg

layout = [
            [sg.Text("Input file:"), sg.Input(key="-IN-"), sg.FileBrowse()],
            [sg.Text("Output Folder:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
            [sg.Exit(), sg.Button("Convert o CSV")],
            [sg.Output(size=(60, 10))]
]

window = sg.Window('maqueico', layout)

window.read()


