#Will C.
#Python 1
#Unit 1, Mod 4.2

#Task 1
# [ ] print "\\\WARNING!///"
print("\\\\\\WARNING!///")
# [ ] print output that is exactly (with quotes): "What's that?" isn't a specific question.
print("\"What's that?\" isn't a specific question.")
# [ ] from 1 print statement output the text commented below using no spaces
# One     Two     Three
# Four    Five    Six
print("One\tTwo\tThree\nFour\tFive\tSix")

#Task 2
# [ ] create and test pre_word()
def pre_word(word):
    if word.isalpha()==True:
        print("Input is a word.")
        wordIsAlpha=True
    else:
        print("Input is not a word.")
        wordIsAlpha=False
        quit()
    if wordIsAlpha==True:
        doPreCheck=True
    else:
        doPreCheck=False
    if doPreCheck==True:
        preCheck=word.startswith("pre")
    else:
        preCheck=False
    if preCheck==True:
        print("Input starts with pre.")
    else:
        print("Input does not start with pre.")
word=input("Input a word that starts with pre: ").lower()
pre_word(word)

#Task 3
# [ ] review, run, fix
#print("Hello" + \n + "World!")
print("Hello\nWorld!")