import sqlite3

# criar uma conexão com o banco de dados
def criar():
    conn = sqlite3.connect('tabelafrutas.db')
    conn.execute('''CREATE TABLE frutas (fruta text, vencimento text, preço real)''')
    conn.commit()
    conn.close()

criando = criar()
criando




