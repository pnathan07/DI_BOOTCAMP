import psycopg2

DBNAME = "postgres"
USER = "postgres"  # postgres
PASSWORD = "cluster"  # <YOUR POSTGRES PASSWORD>
HOST = "localhost"
PORT = "5432"

connection = psycopg2.connect(
    dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT
)

cursor = connection.cursor()

new_db_name = "new_database"

cursor.execute(f"create database {new_db_name};")

connection.commit()

connection.close()
