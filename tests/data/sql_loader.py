import sqlite3

def load_test_data(db_path, data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursos()
    cursor.executemany("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", data)
    conn.commit()
    conn.close()

