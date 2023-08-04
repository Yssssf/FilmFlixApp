from connect import *

def update():
    
    idField = input("Enter FilmID of the record to be updated: ")

   
    fieldName = input("Enter the field name: ").title()
    
    fieldValue = input(f"Enter the value for {fieldName} field: ")


    fieldValue = "'" +fieldValue+ "'"

    
    dbCursor.execute(f"UPDATE tblfilms SET {fieldName} = {fieldValue} WHERE filmID = {idField}")
    dbCon.commit()

    print(f"Record {idField} updated in films table")
if __name__=="__main__":
    update()
