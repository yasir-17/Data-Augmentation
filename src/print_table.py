import sqlite3

def print_table(db_name, table_name):
    # Connect to the database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Execute a SELECT statement to retrieve all rows from the table
    cursor.execute(f"SELECT * FROM {table_name}")

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the connection
    conn.close()