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
        print(lettersForGeneration)
        name=name+string
elif yOrN.lower()=="n":
    while True:
        print("Ok")
        randomNumber=random.randint(1,101)
        if randomNumber==67:
            quit()
        else:
            pass
else:
    print("Input not understood.")
    quit()
print(name.title())