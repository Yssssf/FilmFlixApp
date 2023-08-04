from connect import *
def idField():
    genre = input("Enter the name of the genre to search for: ")
    dbCursor.execute(f"SELECT * FROM tblfilms WHERE genre ='{genre}'").fetchall
    records = dbCursor.fetchall() 
    for aRecord in records:
        print(aRecord)
if __name__=="__main__":
    idField()