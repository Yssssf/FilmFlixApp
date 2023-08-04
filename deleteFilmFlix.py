from connect import *

def deleteFilm():
    idField = input("Enter FilmID of the record to be deleted: ")
    dbCursor.execute("DELETE FROM tblfilms WHERE filmID = {idField}")
    dbCon.commit()
    print(f"Record {idField} deleted from film table")
if __name__ =="__main__":
    deleteFilm()
    dbCon.close()