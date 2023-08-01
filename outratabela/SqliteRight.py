import sqlite3

conn = sqlite3.connect('tabelafrutas.db')
linhas = conn.execute("SELECT frutas.fruta, frutas.vencimento, frutas.preço, verduras.verduras \
                      FROM frutas \
                      RIGHT JOIN verduras ON frutas.fruta=verduras.verduras")

for i in linhas:
    print(i)

conn.close()