import sqlite3

conn = sqlite3.connect('tabelafrutas.db')
conn.execute('''CREATE TABLE verduras (verdura text, vencimento text, preço real)''')
conn.execute("INSERT INTO verduras VALUES('alface', '05-08-2023', '1.50')")
conn.execute("INSERT INTO verduras VALUES('couve', '05-08-2023', '2.00')")
conn.execute("INSERT INTO verduras VALUES('coentro', '05-08-2023', '1.00')")
conn.commit()
conn.close()