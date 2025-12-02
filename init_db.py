import sqlite3
import os
import json

# Eerst config.json inlezen
with open("config.json") as f:
    config = json.load(f)

# Pad naar de database ophalen uit de configuratie
db_path = config["database_path"]
# db_path = "./data/films.db"

# Zorg dat de database-map bestaat
os.makedirs(os.path.dirname(db_path), exist_ok=True)

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Tabel genres
cur.execute("""
CREATE TABLE IF NOT EXISTS genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

# Tabel films
cur.execute("""
CREATE TABLE IF NOT EXISTS films (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    year INTEGER,
    genre_id INTEGER,
    FOREIGN KEY(genre_id) REFERENCES genres(id)
)
""")

# Voeg voorbeeldgenres toe
cur.execute("SELECT COUNT(*) FROM genres")
if cur.fetchone()[0] == 0:
    cur.execute("INSERT INTO genres (name) VALUES ('Actie'), ('Horror')")

# Voeg voorbeeldfilms toe
cur.execute("SELECT COUNT(*) FROM films")
if cur.fetchone()[0] == 0:
    films = [
        ("The Fast and the Furious", 2001, 1),
        ("2 Fast 2 Furious", 2003, 1),
        ("The Conjuring", 2013, 2)
    ]
    for title, year, genre_id in films:
        sql = f"INSERT INTO films (title, year, genre_id) VALUES ('{title}', {year}, {genre_id})"
        cur.execute(sql)
    print("Films toegevoegd aan de database")

conn.commit()
conn.close()
