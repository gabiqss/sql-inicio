import sqlite3

# criar uma conexão com o banco de dados
def apagar():
    conn = sqlite3.connect('tabelafrutas.db')
    conn.execute("DELETE from frutas WHERE fruta = 'melão'")
    conn.commit()
    conn.close()

apagando = apagar()
apagando