#BIBLIOTECA DO BANCO

#VERIFICA LOGIN
import sqlite3


#verifica o login digitado
def verifica_login(login1):
    
    con = sqlite3.connect('primeiro_banco.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users WHERE login = ?", [login1])
    pessoa = cursor.fetchone()   
    con.commit()
    con.close()
    return pessoa
    

#CADASTRA LOGIN