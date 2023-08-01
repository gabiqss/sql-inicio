import sqlite3

# criando conexão com banco de dados
conn = sqlite3.connect('mydatabase.db')

# inserindo dados na tabela
conn.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100,35.14)")
conn.execute("INSERT INTO stocks VALUES ('2006-03-25', 'BUY', 'IBM', 1000,45.00)")
conn.execute("INSERT INTO stocks VALUES ('2006-04-06', 'SELL', 'IBM', 500,53.00)")

# salvar as alterações
conn.commit()

# fechar a conexão
conn.close()