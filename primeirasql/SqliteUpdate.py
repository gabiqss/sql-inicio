import sqlite3

# criar uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

# atualizar dados na tabela
conn.execute("UPDATE stocks SET price = 53.00 WHERE symbol = 'RHAT'")

# salvar as alterações
conn.commit()

# fechar a conexão com o banco de dados
conn.close()