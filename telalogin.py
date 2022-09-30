import sqlite3
import biblioteca
import PySimpleGUI as sg

#Cria o layout da tela, sempre pensando em linhas
layout = [
    [sg.Text('Usuário')],
    [sg.Input(key = 'usuario')],
    [sg.Text('Senha')],
    [sg.Input(key = 'senha')],
    [sg.Button('Login')],
    [sg.Text('', key = 'mensagem')],
]

#criar uma janela
janela = sg.Window('Login', layout = layout)

#loop de eventos
while True:
    event, values = janela.read()

    #assim que clica no X ele fecha
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        usuario = values['usuario']
        senha = values['senha']

        verifica_user = biblioteca.verifica_login(usuario)
        if verifica_user != None:
            id = verifica_user[0]
            login_user = verifica_user[1]
            senha_user = verifica_user[2]
            if senha == senha_user:
                janela['mensagem'].update('Login Feito com sucesso!')
            else:
                janela['mensagem'].update('Senha incorreta!')
        else:
            janela['mensagem'].update('Usuário incorreto!')