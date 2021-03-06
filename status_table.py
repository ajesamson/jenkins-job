import sqlite3


class DbManagement:

    def setup_table(self):
        connection = sqlite3.connect('data.db')

        cursor = connection.cursor()

        query = "CREATE TABLE IF NOT EXISTS job_status (id INTEGER PRIMARY KEY, job text, status_color text, status text, created_at DATE DEFAULT (datetime('now','localtime')))"
        cursor.execute(query)

        connection.commit()
        connection.close()

    def insert_status(self, data):
        connection = sqlite3.connect('data.db')

        cursor = connection.cursor()

        query = "INSERT INTO job_status ('job', 'status_color', 'status') VALUES (?, ?, ?)"
        cursor.executemany(query, data)

        connection.commit()
        connection.close()
