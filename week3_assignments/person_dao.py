import sqlite3

class Person:
    def __init__(self, name, gender, dob, location):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.location = location

class Db_operations:
    def __init__(self):
        self.conn = sqlite3.connect('people.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_db(self):
        pass  # SQLite auto-creates .db file

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS person (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                gender TEXT,
                dob TEXT,
                location TEXT
            )
        ''')
        self.conn.commit()

    def insert_row(self, person):
        self.cursor.execute('''
            INSERT INTO person (name, gender, dob, location)
            VALUES (?, ?, ?, ?)''',
            (person.name, person.gender, person.dob, person.location))
        self.conn.commit()
        return self.cursor.lastrowid

    def search_row(self, id):
        self.cursor.execute('SELECT * FROM person WHERE id = ?', (id,))
        return self.cursor.fetchone()

    def list_all_rows(self):
        self.cursor.execute('SELECT * FROM person')
        return self.cursor.fetchall()

    def update_row(self, updated_person):
        self.cursor.execute('''
            UPDATE person SET name = ?, gender = ?, dob = ?, location = ? WHERE id = ?''',
            updated_person)
        self.conn.commit()

    def delete_row(self, id):
        self.cursor.execute('DELETE FROM person WHERE id = ?', (id,))
        self.conn.commit()