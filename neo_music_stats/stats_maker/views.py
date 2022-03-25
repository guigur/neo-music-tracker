from django.shortcuts import render
import requests
import sqlite3

def stats_maker(request):
    dbname = "neo-diff.sqlite"
    conn = sqlite3.connect(dbname)

    cur = conn.cursor()
    cur.execute("SELECT * FROM musique ORDER BY heureDiffusion DESC LIMIT 20 ")

    rows = cur.fetchall()
    tracks = []

    for row in rows:
        tracks.append({'spotify': row[3], 'trackName': row[0], 'artistName': row[1], 'heureDiffusion': row[2]})
    
    return render(request, 'stats_maker.html', {'tracks': tracks})