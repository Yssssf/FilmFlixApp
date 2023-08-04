from connect import *
def idField():
    rating = input("Enter the rating of film to search for: ")
    dbCursor.execute(f"SELECT * FROM tblfilms WHERE rating ='{rating}'").fetchall
    records = dbCursor.fetchall() 
    for aRecord in records:
        print(aRecord)
if __name__=="__main__":
    idField()