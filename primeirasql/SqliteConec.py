import sqlite3

# criar uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

# criar uma tabela
conn.execute('''CREATE TABLE stocks (data text, trans text, symbol text, qty real, price real)''')

# salvar as alterações
conn.commit()

# fechar a conexão com o banco de dados
conn.close()