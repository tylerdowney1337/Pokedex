import sqlite3

# Create connection to database
conn = sqlite3.connect('pokedex.db')

# Create cursor
c = conn.cursor()

# Execute lookup
c.execute("SELECT rowid, * from pokedex")

items = c.fetchall()

for item in items:
    print(item)

conn.close()
