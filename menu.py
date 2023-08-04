import readFilmFlix,addFilmFlix,deleteFilmFlix,updateFilmFlix,reportFilm,reportGenre,reportRating,reportYears

def menuOptions():
    options = 0
    menuNumbers = "Films Menu Options\nEnter:\n1. Add a record.\n2. Delete a record.\n3. Amend a record.\n4. Print all records.\n5. Exit."
    optionsList = ["1", "2", "3","4", "5"]

    while options not in optionsList: 
        print(menuNumbers)

        options = input("Enter an option from the films main manu!:")

        if options not in optionsList:
            print(f"{options} is not a vali choice in the films menu!")
    return options

def menuOptions2():
    options = 0
    menuNumbers = "Films SubMenu Options\nEnter:\n1. read whole table.\n2. Print details of all films.\n3. Print all films of a particular genre.\n4. Print all films of a particular year.\n5. Print all films of a particular rating. \n6. Exit."
    optionsList = ["1", "2", "3","4", "5","6"]

    while options not in optionsList: 
        print(menuNumbers)

        options = input("Enter an option from the FilmFlix Sub manu!:")

        if options not in optionsList:
            print(f"{options} is not a vali choice in the films menu!")
    return options


mainProgram = True

while mainProgram:
   
    mainMenu = menuOptions()
    if mainMenu == "1":
        addFilmFlix.insertFilm()
    elif mainMenu == "2":
        deleteFilmFlix.deleteFilm()
    elif mainMenu == "3":
        updateFilmFlix.update()
    elif mainMenu == "4":
        subManu = True
        while subManu:
            subManu = menuOptions2()
            if subManu =="1":
                readFilmFlix.read()
            elif subManu =="2":
                reportFilm.idField()
            elif subManu == "3":
                reportGenre.idField()
            elif subManu =="4":
                reportRating.idField()
            elif subManu =="5":
                reportYears.idField()   
            else:
                subManu =False       
    else:
        mainProgram = False
input("Press enter to quit the Films application")
