import sqlite3

# connection = sqlite3.connect(':memory:')  # database de teste
connection = sqlite3.connect('ERP/database/database.db')
cursor = connection.cursor()

# DATATYPES: null, integer, real(float), text, blob(images)

table_name_Itens = 'Itens'
table_qtd_Itens = 8
# cursor.execute("""CREATE TABLE Itens (
#     Item_ID text,
#     Name text,
#     Description text,
#     Image text,
#     Category text,
#     Supplier text,
#     Purchase_Cost float,
#     Sale_Price float
#     )
# """)  # possui 8 itens

table_name_Suppliers = 'Suppliers'
table_qtd_Suppliers = 7
# cursor.execute("""CREATE TABLE Suppliers (
#     Supplier_ID text,
#     Name text,
#     Logo blob,
#     Website text,
#     Phone text,
#     Email text,
#     Address text
#     )
# """)  # possui 7 itens

table_name_Inventory = 'Inventory'
table_qtd_Inventory = 5
cursor.execute("""CREATE TABLE Inventory (
    Inventory_ID text,
    Item_ID text,
    Date text,
    Time text,
    Amount int
    )
""")  # possui 5 itens

connection.commit()
connection.close()