import os
counter = 0
while True:
    answer=input("Would you like to install Borat? [Y or N]\n")
    if answer.lower()=="y":
        print("Good.")
        break
    elif answer.lower()=="n":
        print("That is not an option.")
os.mkdir("Borat")
os.chdir("Borat")
while True:
    open(("Borat"+str(counter)+".txt"),"w")
    counter+=1