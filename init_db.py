import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as file:
    connection.executescript(file.read())

connection.execute('insert into users (name, age, image) values (?, ?, ?)',
                   ('Guido', 23, 'https://randomuser/me/api/portraits/men/40.jpg')
                   )
connection.execute('insert into users (name, age, image) values (?, ?, ?)',
                   ('Sandra', 25, 'https://randomuser/me/api/portraits/women/27.jpg')
                   )
connection.execute('insert into users (name, age, image) values (?, ?, ?)',
                   ('Michael', 28, 'https://randomuser/me/api/portraits/men/32.jpg')
                   )

connection.commit()

connection.close()
