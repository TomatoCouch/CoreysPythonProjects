#Will C.
#Python 1
#Final Project, standard 2.02

import datetime

#Standard 2.02: Sequence Manipulation
counter=0
listAgain=["this is the ",4,"th list I've made today (",datetime.date(2022,5,27),")"]
for item in listAgain:
    print(listAgain[counter],end="")
    counter+=1
listEntryOne=listAgain[0]
listEntryThree=listAgain[2]
print()
print(listEntryThree[18:23],listEntryOne[5:7],listAgain[3])