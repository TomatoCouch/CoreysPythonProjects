#Will C.
#Python 1
#Final Project, Standard 1.01
#Sit tight, you'll be here a while.

#Standard 1.01: Python and Jupyter Basics
#Funny story we never used Jupyter in class
#so uh
#Hey look I created a couple Python scripts that I'll just show off here

#Random Name Generator:
import random
lettersForGeneration=["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
name=""
counter=0
print("Random name generator!\nWould you like to generate a name?")
yOrN=input("[Y/N]\n")
if yOrN.lower()=="y":
    print("Great!")
    for string in lettersForGeneration:
        random.shuffle(lettersForGeneration)
        name=name+string
elif yOrN.lower()=="n":
    while True:
        print("Ok")
        randomNumber=random.randint(1,101)
        if randomNumber==67:
            break
        else:
            pass
else:
    print("Input not understood.")
print(name.title())
#I actually got the first name "Alex" out of this once.

#Radians to Degrees converter:
#Degrees -> Degrees by default
from cmath import pi
print("Will's Degree/Radian calculator!")
doRad=False
doDeg=True
while True:
    if doDeg==True and doRad==False:
        num=input("Enter your degrees. To quit, enter quit. To switch conversion, enter swap. If you'd like pi to remain in your answers, enter pi. ")
        if num.lower()=="quit":
            break
        elif num.lower()=="swap":
            doDeg=False
            doRad=True
        elif num.lower()=="pi":
            while True:
                print("no")
        else:
            try:
                print(num,"degrees is equivalent to:",float(num)*(pi/180.0),"radians.")
            except ValueError:
                print("You can't convert a letter to a float.")
    elif doDeg==False and doRad==True:
        num=input("Enter your radians. To quit, enter quit. To switch conversion, enter swap. If you'd like pi to remain in your answers, enter pi. ")
        if num.lower()=="quit":
            break
        elif num.lower()=="swap":
            doDeg=True
            doRad=False
        elif num.lower()=="pi":
            while True:
                print("no")
        else:
            print(num,"radians is equivalent to:",float(num)*(180.0/pi),"radians.")
#I couldn't figure out how to get it to conserve pi, but I hate pi, so I don't care :)

#Risk of Rain 2 character selector
from random import shuffle
from random import randint
survivorList=["Commando","Huntress","Bandit","Mul-T","Engineer","Artificer","Mercenary","REX","Loader","Acrid","Captain","Railgunner","「V??oid Fiend』"]
while True:
    shuffle(survivorList)
    playerList=[]
    while True:
        playerName=input("Enter a player name. To quit, enter nothing. ")
        if playerName=="":
            break
        else:
            playerList.append(playerName)
            print("Players:\n",playerList)
    for name in playerList:
        randomInteger=randint(0,13)
        print(name,":\n",survivorList[randomInteger])
    keep=input("Is this satisfactory? ")
    if keep.lower()=="yes":
            break
    else:
            pass
#Risk of Rain 2 is a game me and my friends play often, but we have the issue of being unable to choose which character to play.
#I fixed that.

#TF2 Matchup Maker
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
#TF2 is pretty fun

#End showcase.