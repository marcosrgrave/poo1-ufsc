import sqlite3

# connection = sqlite3.connect(':memory:')  # database de teste
connection = sqlite3.connect('ERP/database/database.db')
cursor = connection.cursor()

# INSERINDO VARIOS ITENS (LINHAS) DE UMA VEZ SÓ
many_tuples = (
    (
        "0001",
        "Saw",
        "Battery powered circular saw",
        "Items_Images/item-123.Image.211420.png",
        "Category 01",
        "Vendor 01",
        "$49.00",
        "$72.00"
    ),
    (
        "0002",
        "Hammer",
        "Framing hammer",
        "Items_Images/item-345.Image.211436.png",
        "Category 01",
        "Vendor 01",
        "$7.00",
        "$15.00"
    ),
    (
        "0003",
        "T-Square",
        "T-square with metric ruler",
        "Items_Images/item-567.Image.211512.png",
        "Category 01",
        "Vendor 01",
        "$9.00",
        "$18.00"
    )
)

cursor.executemany(
    f"INSERT INTO Itens VALUES (?,?,?,?,?,?,?,?)", many_tuples
)

connection.commit()
connection.close()