import sqlite3


import sqlite3

from numpy import concatenate

# connection = sqlite3.connect(':memory:')  # database de teste
connection = sqlite3.connect('ERP/database/database.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE fornecedores (
    name text,
    email text,
    phone text,
    website text,
    address text
    )
""")

cursor.execute("""CREATE TABLE produtos (
    name text,
    supplier text,
    cost real,
    price real,
    qtd int
    )
""")

connection.commit()
connection.close()