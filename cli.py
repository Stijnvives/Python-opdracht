import sqlite3
import csv
import json
import os
from models.film import Film

# Config laden
with open("config.json") as f:
    config = json.load(f)

db_path = config["database_path"]

# FUNCTIES
def list_films():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT films.id, films.title, films.year, genres.name
        FROM films
        LEFT JOIN genres ON films.genre_id = genres.id
    """)
    rows = cur.fetchall()
    conn.close()

    print("\nID | Titel | Jaar | Genre")
    print()
    for r in rows:
        film = Film(*r)
        print(film)

def add_film():
    title = input("Titel van de film: ")
    year = input("Jaar van de film: ")
    genre_id = input("Genre ID (1=Actie, 2=Drama): ")

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO films (title, year, genre_id) VALUES (?, ?, ?)",
        (title, year, genre_id)
    )
    conn.commit()
    conn.close()

    print(f"Film '{title}' toegevoegd!")

def delete_film():
    list_films()
    film_id = input("ID van de film die je wilt verwijderen: ")

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DELETE FROM films WHERE id = ?", (film_id,))
    conn.commit()
    conn.close()

    print(f"Film met ID {film_id} verwijderd!")

def export_csv():
    filename = input("Naam van het CSV bestand (bv. films.csv): ")

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT films.id, films.title, films.year, genres.name
        FROM films
        LEFT JOIN genres ON films.genre_id = genres.id
    """)
    rows = cur.fetchall()
    conn.close()
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Title", "Year", "Genre"])
        writer.writerows(rows)

    print(f"CSV geëxporteerd naar {filename}")

def main():
    while True:
        print("\n---- Filmtool ----")
        print("1. Lijst films tonen")
        print("2. Film toevoegen")
        print("3. Film verwijderen")
        print("4. Exporteren naar CSV")
        print("5. Stoppen")

        keuze = input("Maak een keuze (1-5): ")

        if keuze == "1":
            list_films()
        elif keuze == "2":
            add_film()
        elif keuze == "3":
            delete_film()
        elif keuze == "4":
            export_csv()
        elif keuze == "5":
            print("Programma gestopt.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main()
