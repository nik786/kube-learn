import sqlite3 as sql
db_path = 'worldevents.db'

# Connect to the SQLite database (this will create the database if it does not exist)
conn = sql.connect(db_path)

# Check if the table exists
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='world_events';")
table_exists = cursor.fetchone()

# If the table doesn't exist, create it from the DataFrame
if not table_exists:
    df.to_sql('world_events', conn, index=False)
    print("Table 'world_events' created and data inserted.")
else:
    print("Database and table 'world_events' already exist.")
