import sqlite3

# criar uma conexão com o banco de dados
conn = sqlite3.connect('mydatabase.db')

# selecionar todos os dados da tabela
cursor = conn.execute('SELECT * from stocks')

# iterar sobre os dados e exibi-los
for row in cursor:
    print(row)

# fechar a conexão com o banco de dados
conn.close()