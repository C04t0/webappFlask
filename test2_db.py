import sqlite3

# Maak een SQLite-verbinding en stel row factory in op sqlite3.Row
conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row

# Maak een cursor en voer een query uit
curs = conn.cursor()
curs.execute('SELECT * FROM users')

# Haal de eerste rij op
result = curs.fetchone()
print(type(result))

# Het resultaat is nu een Row-object in plaats van een standaard tuple
print(result.keys())  # Geeft de kolomnamen terug
print(result['name'])  # Toegang tot kolomwaarde via kolomnaam
print(result[2])  # Toegang tot kolomwaarde via index

# Sluit de verbinding
conn.close()
