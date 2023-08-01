import sqlite3

# criar uma conexão com o banco de dados
def ler():
    conn = sqlite3.connect('tabelafrutas.db')
    linhas = conn.execute("SELECT * from frutas")
    for i in linhas:
        print(i)
    conn.close()

lendo = ler()
lendo