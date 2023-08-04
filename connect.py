import sqlite3

dbCon = sqlite3.connect(r"week11\filmflix.db")

dbCursor = dbCon.cursor()