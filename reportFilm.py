from connect import *
def idField():
    title = input("Enter the name of the title to search for: ")
    dbCursor.execute(f"SELECT * FROM tblfilms WHERE title ='{title}'").fetchall
    records = dbCursor.fetchall() 
    for aRecord in records:
        print(aRecord)
if __name__=="__main__":
    idField()