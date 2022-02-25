import sqlite3

# connection = sqlite3.connect(':memory:')  # database de teste
connection = sqlite3.connect('ERP/database/database.db')
cursor = connection.cursor()

# cursor.execute(
#     'SELECT rowid, * FROM Itens'
# )

cursor.execute('SELECT * FROM Itens WHERE Purchase_Cost >= 8')

intens = cursor.fetchall()
for item in intens:
    print(item)

connection.commit()
connection.close()