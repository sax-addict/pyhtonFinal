import os
import pathlib
os.system('cls')

def GetState():
    gstate = input("Name a state: ")
    return gstate

def FormatState(fstate):
    lenState = len(fstate)
    if lenState < 8:
        lstate = fstate.ljust(8)
        return lstate
    else:
        return fstate

print("1. Get information and display to screen")
print("2. Call user created functions")
print("3. Write List of files to file")
print("4. Read specified file")
print("")
task = input("Enter number of task to do: ")
task = int(task)


if task == 1:
    companyName = "Dunwoody College"
    programName = "Computer Networking"
    uName = os.environ['Username']
    classFirst = input("Name of First Class: ")
    classSecond = input("Name of Second Class: ")
    print("At "+companyName+", "+uName+" is in the "+programName+" program")
    print("First Class: "+ classFirst)
    print("Second class: "+classSecond)
elif task == 2:
    state = GetState()
    newState = FormatState(state)
    print(newState+" is at least 8 characters long, while "+state+" could be shorter")
elif task == 3:
    fileName = input("File name: ")
    fList = []
    dList = []
    for p in pathlib.Path('.').iterdir():
        if p.is_file():
            fList.append(p)
        else:
            dList.append(p)
    with open(fileName, "w") as myFileWrite:
        myFileWrite.write("These are my files:\n")
        for f in fList:
            myFileWrite.write(f.name)
            myFileWrite.write("\n")
        myFileWrite.write("\n")
        myFileWrite.write("These are my directories:\n")
        for f in dList:
            myFileWrite.write(f.name)
            myFileWrite.write("\n")

elif task == 4:
    txtFile = input("Which file would you like to read? ")
    with open(txtFile, "r+") as myFileRead:
        print(myFileRead.read())
else:
    print("not valid")