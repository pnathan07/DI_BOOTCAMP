import psycopg2

# 1. Create a connection with the database (hollywood)

# IF ALL LETTERS ARE UPPERCASE - THEN ITS A CONSTANT (not meant to change)
DBNAME = "hollywood"
USER = "postgres"  # postgres
PASSWORD = "cluster"  # <YOUR POSTGRES PASSWORD>
HOST = "localhost"
PORT = "5432"


# 3. Run SELECT queries


def select_all(table: str, cursor) -> list[tuple]:

    query = f"select * from {table};"
    cursor.execute(query)
    rows = (
        cursor.fetchall()
    )  # if the query returns something (like select) - fetch all of the rows returned

    return rows


# # 4. Run UPDATE queries


def update_values_single_field(
    table: str,
    field: str,
    new_value: str,
    search_by_field,
    search_by_value,
    cursor,
    connection,
):

    query = f"UPDATE {table} SET {field} = %s where {search_by_field} = %s;"
    cursor.execute(query, (new_value, search_by_value))
    connection.commit()  # apply all changes from cursor through the connection


# # 5. Run Create table


def create_table(table_name: str, cursor, connection):
    query = "create table %s (id serial primary key, name varchar(50));"
    cursor.execute(query, table_name)
    connection.commit()


def main():

    with psycopg2.connect(
        dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT
    ) as connection:  # context manager

        # 2. Create a cursor (tool to run queries)
        cursor = connection.cursor()

        update_values_single_field(
            table="property",
            field="city",
            new_value="TLV",
            search_by_field="id",
            search_by_value="3",
            cursor=cursor,
            connection=connection,
        )
    # once we finished running queries - the connection is automatically closed


if __name__ == "__main__":
    main()
