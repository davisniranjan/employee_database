import sqlite3

# Connect to the database (if the database doesn't exist, it will be created)
conn = sqlite3.connect('employee.db')

# Create a cursor to interact with the database
cursor = conn.cursor()

# Create an employee table with columns (id, name, designation, salary)
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    designation TEXT NOT NULL,
                    salary REAL NOT NULL
                )''')

# Commit changes and close the connection
conn.commit()
conn.close()
