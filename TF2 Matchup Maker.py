from random import randint
from random import shuffle
counter=0
redTeam=[]
bluTeam=[]
mercList=["Scout","Soldier","Pyro","Demoman","Heavy","Engineer","Medic","Sniper","Spy"]
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
while True:
    try:
        redNum=int(input("How many players are on Red team? "))
    except ValueError:
        print("Numbers only, please.")
    else:
        break
while redNum!=counter:
    mercIndex=randint(0,8)
    shuffle(mercList)
    redTeam.append(mercList[mercIndex])
    counter+=1
counter=0
while True:
    try:
        bluNum=int(input("How many players are on Blu team? "))
    except ValueError:
        print("Numbers only, please.")
    else:
        break
while bluNum!=counter:
    mercIndex=randint(0,8)
    shuffle(mercList)
    bluTeam.append(mercList[mercIndex])
    counter+=1
print("Red Team:\n",redTeam)
print("Blu Team:\n",bluTeam)