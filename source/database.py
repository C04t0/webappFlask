import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_connection(self):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = sqlite3.Row
        return connection

    def get_all_users(self):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            return cursor.execute('select * from users').fetchall()

    def get_user(self, user_id):
        with self.create_connection() as conn:
            cursor = conn.cursor()
            return cursor.execute('select * from users where id = ?', (user_id,)).fetchone()

    def add_user(self, parameters):
        with self.create_connection() as conn:
            conn.execute('insert into users (name, age, image) values (?, ?, ?)', parameters)
            conn.commit()

    def update_user(self, parameters):
        with self.create_connection() as conn:
            conn.execute('update users set name=?, age=? where id=?', parameters)
            conn.commit()

    def delete_user(self, user_id):
        with self.create_connection() as conn:
            conn.execute('delete from users where id = ?', (user_id))
            conn.commit()