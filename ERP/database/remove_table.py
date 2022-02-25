import sqlite3

# connection = sqlite3.connect(':memory:')  # database de teste
connection = sqlite3.connect('ERP/database/database.db')
cursor = connection.cursor()

table_name = 'fornecedores'  # name of the table to be deleted

cursor.execute(
    f'''DROP TABLE {table_name}'''
)

connection.commit()
connection.close()