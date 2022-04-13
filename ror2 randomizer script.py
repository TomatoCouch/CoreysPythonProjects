from random import shuffle
from random import randint
survivorList=["Commando","Huntress","Bandit","Mul-T","Engineer","Artificer","Mercenary","REX","Loader","Acrid","Captain","Railgunner","「V??oid Fiend』"]
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