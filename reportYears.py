from connect import *
def idField():
    year = input("Enter year of the film to search for: ")
    dbCursor.execute(f"SELECT * FROM tblfilms WHERE yearReleased ='{year}'").fetchall
    records = dbCursor.fetchall() 
    for aRecord in records:
        print(aRecord)
if __name__=="__main__":
    idField()