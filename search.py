from pyrsistent import v
import requests
from pprint import pprint
import sqlite3

dbname = "neo-diff.sqlite"
conn = sqlite3.connect(dbname)

cur = conn.cursor()
cur.execute("SELECT * FROM musique")

rows = cur.fetchall()


def getIdFromSpotify(searchStr):
    security = {'Authorization': 'Bearer ' + 'BQDsUrPIrtF6I94oCgGyhNv-71p4u7gbYE_RFs-9bQUj_JuFWUjKWYkDfupSFcA0oPdUzFa4sgwJaWSS8giNqP_A11sF7GGhrSECe35NiAJpZaKpH6O_DdN70hGZIDLuzPrV1SQD-Q' }
    r = requests.get('https://api.spotify.com/v1/search', params={'q': searchStr, 'type': 'track', 'market': 'FR', 'limit': '1'}, headers=security)
    try:
        spotifydata = r.json()['tracks']['items'][0]['id']
    except:
        print("Exception thrown. x does not exist.")
        spotifydata = ""
    print(r.status_code)
    return (spotifydata)


for row in rows:
    print(getIdFromSpotify(row[0] + ' ' + row[1]))