#Will C.
#Python 1
#Final Project, Standard 1.02

#Standard 1.02: Functions
#I'm just gonna assume that means defining functions
def simpleFunction(word,number):
    #Function will add the length of a word with another number.
    wordLen=len(word)
    total=wordLen+number
    return total
functionWord=input("Enter a word. ")
functionNumber=int(input("Enter a number. "))
print(simpleFunction(functionWord,functionNumber))