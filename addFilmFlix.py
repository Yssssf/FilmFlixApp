from connect import *
def insertFilm():
    tblfilms =[]

    filmID = input("Enter your Film ID:")
    title = input("Enter Film Title: ")
    yearReleased = input("Enter Film Year: ")
    rating = input("Enter Film Rating: ")
    duration = input("Enter Film Time: ")
    genre = input("Enter Film Genre: ")

    tblfilms.append(filmID)
    tblfilms.append(title)
    tblfilms.append(yearReleased)
    tblfilms.append(rating)
    tblfilms.append(duration)
    tblfilms.append(genre)

    dbCursor.execute("INSERT INTO tblfilms(filmID,title,yearReleased,rating,duration,genre) VALUES(?,?,?,?,?,?)",tblfilms)
    dbCon.commit()

    print(f"{title} inserted into FilmFlix")

if __name__=="__main__":
    insertFilm()
