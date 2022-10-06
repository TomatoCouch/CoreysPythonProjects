#Will C.
#Python 1
#Final Project, Standard 2.03

#Standard 2.03: Sequence Iteration
counter=0
sentence="I've done these so many times I could actually do it in my sleep."
while counter != len(sentence):
    print(sentence[counter],end=" ")
    counter+=1
print("\n")
#But that's not the only way!
counter=0
while True:
    try:
        print(sentence[counter],end="")
    except IndexError:
        break
    finally:
        counter+=1
print("\n")
#and maybe it'll work if I do it this way?
counter=0
while sentence[counter]!=sentence[-1]:
    print(sentence[counter])
    counter+=1
print('.')