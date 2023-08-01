import sqlite3

# criar uma conexão com o banco de dados
def atualizar():
    conn = sqlite3.connect('tabelafrutas.db')
    conn.execute("UPDATE frutas SET preço = 2.00 WHERE fruta = 'laranja'")
    conn.commit()
    conn.close()

atualizando = atualizar()
atualizando