#Will C.
#Python 1
#Unit 2, Mod 3.4

#Task 1
# [ ] split the string(rhyme) into a list of words (rhyme_words) 
# [ ] print each word on it's own line 
rhyme = 'Jack and Jill went up the hill To fetch a pail of water' 
rhymeWords=rhyme.split()

for word in rhymeWords:
    print(word)
# [ ] split code_tip into a list and print the first and every other word 
code_tip = "Python uses spaces for indentation" 
codeTipWords=code_tip.split()

for word in codeTipWords:
    print(word)

#Task 2
# [ ] split poem into a list of phrases by splitting on "*" a 
# [ ] print each phrase on a new line in title case 
poem = "Write code frequently*Save code frequently*Comment code frequently*Study code frequently*" 
poemPhrases=poem.split("*")

#Task 3
# [ ] .join() letters list objects with an Asterisk: "*" 
letters = ["A", "s", "t", "e", "r", "i", "s", "k"]
print("*".join(letters))

#Task 4
#get user input on what to use to join words (" ", *, -, etc...) - store in variable: separator
#join pharse_words with the separator and print
# [ ] complete Choose the separator 
phrase_words = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill', 'To', 'fetch', 'a', 'pail', 'of', 'water']
separator=input("How would you like your words seperated? ")
print(separator.join(phrase_words))

#Task 5
# [ ] use 3 print() statements to output text to one line  
# [ ] separate the lines by using "- " (dash space)
print("This string",end="- ")
print("is three",end="- ")
print("lines long.")

#Task 6
# [ ] create a string (fact) of 20 or more characters and cast to a list (fact_letters)
fact="ooga booga ping pong banana"
factLetters=list(fact)
# [ ] iterate fact, printing each char on one line, except for spaces print a new line
for letter in factLetters:
    if letter==" ":
        pass
    else:
        print(letter)

#Task 7
#Create a 20 digit string, and cast to a list
#Then add all the digits as integers
#Print the equation and answer
#Hint: use cast to sum the digits, and .join() to create the equation (1+2+3+...)
twentyDigitString=("11111111111111111111")
twentyDigitList=list(twentyDigitString)
sum=0
for number in twentyDigitList:
    sum+int(number)
    print(sum)
    print(number)
print(" + ".join(twentyDigitList),"= ",sum)