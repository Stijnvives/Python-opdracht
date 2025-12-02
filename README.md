# Filmtool

## Beschrijving
Filmtool is een eenvoudige command line applicatie om films te beheren.  
Je kunt films toevoegen, verwijderen, opvragen en exporteren naar een CSV-bestand.  
De gegevens worden opgeslagen in een SQLite-database.

## Structuur van het project
- `cli.py` --> Hoofdscript met het menu voor de gebruiker  
- `init_db.py` --> Script om de database aan te maken en voorbeelddata in te voegen  
- `models/film.py` --> Klasse `Film`  
- `services/db_services.py` --> Functies voor database-interactie (lijst, toevoegen, verwijderen, exporteren)  
- `config.json.example` --> Voorbeeldconfiguratie voor de database  
- `requirements.txt` --> Pakkettenlijst (standaard modules worden gebruikt)  
- `venv/` --> Virtual environment (niet in Git)  
- `data/` --> Bevat de SQLite-database (niet in Git)  

## Installatie
```bash
1. Open een terminal(CMD, PowerShell, Git Bash,...) en ga naar de map waar je het project wilt plaatsen:
VB CMD: cd C:\Users\Stijn\mapfilms
VB Powershell: cd "C:\Users\Stijn\mapfilms"
VB Git Bash: cd "C:\Users\Stijn\mapfilms"

2. Clone de repository:
git clone <repo-url>
cd Python-opdracht


3. Virtuele omgeving aanmaken en activeren:
Windows:
python -m venv venv
venv\Scripts\activate


Linux/Mac:
python -m venv venv
source venv/bin/activate

4. Pakketten installeren(optioneel):
pip install -r requirements.txt
Voor deze applicatie zijn geen extra pakketten nodig, alleen standaard Python modules.


5. Configuratiebestanden aanmaken
Kopieer config.json.example naar config.json
Pas eventueel het pad van de database aan:

{
    "database_path": "./data/films.db"
}


6. Database aanmaken met voorbeeldfilms
python init_db.py


7. CLI starten
python cli.py

8. Menu opties

1: Lijst films tonen
2: Film toevoegen
3: Film verwijderen
4: Exporteren naar CSV
5: Stoppen


.gitignore bevat:
venv/
data/
config.json















