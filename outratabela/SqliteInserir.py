import sqlite3

# criar uma conexão com o banco de dados
def inserir():
    conn = sqlite3.connect('tabelafrutas.db')
    conn.execute("INSERT INTO frutas VALUES('maçã', '05-08-2023', '1.00')")
    conn.execute("INSERT INTO frutas VALUES('laranja', '05-08-2023', '1.50')")
    conn.execute("INSERT INTO frutas VALUES('melão', '05-08-2023', '4.00')")
    conn.commit()
    conn.close()

inserindo = inserir()
inserindo

