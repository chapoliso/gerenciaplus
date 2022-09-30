import sqlite3
import biblioteca

print('Seja bem Vindo a tela de Login!')

login = input('Login: ')
senha = input('Senha: ')

teste = (biblioteca.verifica_login(login))

if teste != None:
    id = teste[0]
    usuario = teste[1]
    senhauser = teste[2]
    if senha == senhauser:
        print('ok')
    else:
        print('senha invalida')
else:
    print('usuario nao encontrado')