#Will C.
#Python 1
#Final Project, Standard 2.00

#Standard 2.00: Understand Python Data Structures
#idk what this means
#uh
counter=0
aList=["hey look","\n","a list!","\n"]
aTuple=("eww,","\n","a tuple.","\n")
aDictionary={0:"dictionaries",1:"are",2:"confusing",3:"and you can just turn them into lists"}
#while writing this program I realized that I could just make the key values integers starting at 0
#thus turning a dictionary into a list

while counter<=3:
    print(aList[counter],end="")
    counter+=1
counter=0
while counter<=3:
    print(aTuple[counter],end="")
    counter+=1
counter=0
while counter<=3:
    print(aDictionary[counter],end="")
    counter+=1