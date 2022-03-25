from pyrsistent import v
import requests
from pprint import pprint
import sqlite3
import neo_spotify_id_agent

dbname = "neo-diff.sqlite"
conn = sqlite3.connect(dbname)

cur = conn.cursor()
cur.execute("SELECT * FROM musique")

rows = cur.fetchall()

for row in rows:
    print(neo_spotify_id_agent.getIdFromSpotify(row[0] + ' ' + row[1]))