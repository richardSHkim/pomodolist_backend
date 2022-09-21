import os
import psycopg2


conn = psycopg2.connect(host="localhost", dbname=os.environ["DB_NAME"], user=os.environ["DB_USER"], password=os.environ["DB_PASS"])


def create_tables():
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS schedules (
                    id BIGSERIAL NOT NULL PRIMARY KEY,
                    time INT NOT NULL)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS todolist (
                    id BIGSERIAL NOT NULL PRIMARY KEY,
                    todo TEXT NOT NULL,
                    done BOOL NOT NULL)''')
    conn.commit()
