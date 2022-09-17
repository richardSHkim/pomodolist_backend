import psycopg2


conn = psycopg2.connect(host="localhost", dbname="pomodolist_db", user="postgres", password="0721")


def create_tables():
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS schedules (
                    time int)''')
    conn.commit()
