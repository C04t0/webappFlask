import sqlite3

# Maak een database Connection-object
connection = sqlite3.connect('database.db')

# Maak een Cursor-object
cursor = connection.cursor()

# Gebruik het Cursor-object voor het uitvoeren van een SQL-query.
# Het resultaat van een query is een 'recordset' (opgeslagen in het Cursor-object).
# De cursor wijst het eerste record in de recordset aan.
cursor.execute('select * from users')

# Haal het eerste record op als een tuple
row = cursor.fetchone()
print(row)
print(type(row))

# Haal het volgende record op (na elke fetch-operatie wordt de cursor verplaatst!)
row = cursor.fetchone()
print(row)

# Haal alle records op als een list van tuples
cursor.execute('select * from users')
rows = cursor.fetchall()
print(rows)

# Itereer over een recordset
for row in rows:
    print(row[2])

# Sluit de database-connectie
connection.close()