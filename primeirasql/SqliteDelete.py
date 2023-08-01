import sqlite3

# criar uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

# apagar dados na tabela
conn.execute("DELETE from stocks WHERE symbol = 'IBM'")

# salvar as alterações
conn.commit()

# fechar conexão

conn.close()