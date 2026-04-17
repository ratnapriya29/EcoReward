import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            result TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_data(filename, result):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("INSERT INTO predictions (filename, result) VALUES (?, ?)", (filename, result))

    conn.commit()
    conn.close()

def get_data():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT * FROM predictions")
    data = c.fetchall()

    conn.close()
    return data