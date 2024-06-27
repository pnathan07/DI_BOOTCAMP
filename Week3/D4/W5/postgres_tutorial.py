import psycopg2

# Windows > pip install psycopg2
# Mac > pip install psycopg2-binary


# 1. Create a connection with the database (hollywood)

# IF ALL LETTERS ARE UPPERCASE - THEN ITS A CONSTANT (not meant to change)
DBNAME = "hollywood"
USER = "postgres"  # postgres
PASSWORD = "cluster"  # <YOUR POSTGRES PASSWORD>
HOST = "localhost"
PORT = "5432"

connection = psycopg2.connect(
    dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT
)

# 2. Create a cursor (tool to run queries)
cursor = connection.cursor()

# 3. Run SELECT queries


def select_all(table: str) -> list[tuple]:

    query = f"select * from {table};"

    cursor.execute(query)

    rows = (
        cursor.fetchall()
    )  # if the query returns something (like select) - fetch all of the rows returned

    return rows


# rows_movies = select_all("movies")

# for row in rows_movies:
#     print(row)

# rows_actors = select_all("actors")

# for row in rows_actors:
#     print(row)


# # 4. Run UPDATE queries


def update_values_single_field(
    table: str, field: str, new_value: str, search_by_field, search_by_value
):

    query = f"UPDATE {table} SET {field} = %s where {search_by_field} = %s;"
    cursor.execute(query, (new_value, search_by_value))
    connection.commit()  # apply all changes from cursor through the connection


# update_values_single_field(
#     table="actors",
#     field="first_name",
#     new_value="George",
#     search_by_field="actor_id",
#     search_by_value="2",
# )


update_values_single_field(
    table="property",
    field="city",
    new_value="TLV",
    search_by_field="id",
    search_by_value="1",
)

# # 5. Run Create table

query = "create table sample_table (id serial primary key, name varchar(50));"
cursor.execute(query)
connection.commit()
