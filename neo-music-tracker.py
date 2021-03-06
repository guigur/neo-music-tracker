import json
import requests
import sqlite3
import time
from datetime import datetime

dbname = "neo-diff.sqlite"

# conn = sqlite3.connect(dbname)
# conn.execute('''CREATE TABLE musique
#                (titreNom          TEXT      NOT NULL,
#                artisteNom         TEXT      NOT NULL,
#                heureDiffusion     timestamp NOT NULL);''')
# conn.close()
# exit()
currentTitreNom = ""
currentArtisteNom = ""

while(True):
    timestamp = datetime.now()
    try:
        r = requests.get('http://www.radioneo.org/liveJSON.json')
        data = r.json()
        if(data["titreNom"] != currentTitreNom and data["artisteNom"] != currentArtisteNom):
            currentTitreNom = data["titreNom"]
            currentArtisteNom = data["artisteNom"]
            print(str(timestamp) + " => Adding to the database : '" + currentTitreNom + "' par : '" + currentArtisteNom + "'")
            conn = sqlite3.connect(dbname)
            conn.execute("insert into musique (titreNom,artisteNom,heureDiffusion) VALUES (?, ?, ?)", (currentTitreNom, currentArtisteNom, str(timestamp)))
            conn.commit()
            conn.close()
        else:
            print("Same song, waiting")
    except:
        print("Error while getting the good stuff")
    time.sleep(30)
