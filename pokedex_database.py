import sqlite3

# Create connection to database
conn = sqlite3.connect('pokedex.db')

# Create cursor
c = conn.cursor()

# Create pokedex table
# c.execute("""CREATE TABLE pokedex (
#    name text,
#    type text,
#    height text,
#    weight text,
#    hp text,
#    attack text,
#    defense text,
#    spatk text,
#    spdef text,
#    speed text
#    img text
#    )""")

# conn.commit()
# conn.close()


# Add data to pokedex.db
# c.execute("""INSERT INTO pokedex VALUES (
    "Mew",
    "Psychic",
    "0.4 m",
    "4.0 kg",
    "100",
    "100",
    "100",
    "100",
    "100",
    "100",
    "151"
    )""")

conn.commit()
conn.close()
