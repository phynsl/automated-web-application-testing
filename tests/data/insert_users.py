import mariadb

def insert_users(users, db_config):
    conn = mariadb.connect(**db_config)
    cursor = conn.cursor()
    for user in users:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (user["username"], user["email"], user["password"])
        )
    conn.commit()
    conn.close()
