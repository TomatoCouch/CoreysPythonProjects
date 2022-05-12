print("TF2 Matchup Maker\nby Will\nEnter [Y] to start. Enter [N] to quit.")
while True:
    instructions=input("")
    if instructions.lower()=="y":
        break
    elif instructions.lower()=="n":
        while True:
            print("No")
    else:
        print("Input not understood.")
redNum=input("How many players are on Red team?")