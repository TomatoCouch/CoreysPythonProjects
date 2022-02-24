#Will C.
#Python 1
#Unit 1, mod 4.1

#Task 1
# [ ] Say "Hello" with nested if
greet=input("Would you like to greet someone? 'y' or 'n': ")
if greet.lower()=='y':
    greet_type=input("Would you like to say hello, or just hi? 'y' or 'n': ")
    if greet_type.lower()=="y":
        print("Hello!")
    else:
        print("Hi!")
elif greet.lower()=="n":
    print("Ok")
else: 
    print("Unexpected input.")
# [ ] Challenge: handle input other than y/n
#Done

#Task 2
# [ ] Create the "Guess the bird" program
print("Guess The Bird!")
do_start=input("Would you like to play? ")
if do_start.lower()=="y":
    print("Great! ")
    start=True
elif do_start.lower()=="yes":
    print("Great! ")
    start=True
else:
    print("Too bad.")
    startBad=True
birds="cardinal bluejay tit"
if start==True:
    print("Rules:")
    print("")
    print("3 birds have been named. Guess one of the 3 to win!")
    doQuestions=True
elif startBad==True:
    print("Rules:")
    print("")
    print("Since you don't want to do this, you get one shot. Name one of the 3 birds I've selected, then get out of here.")
    doQuestionsBad=True
else:
    print("how")
if doQuestions==True:
    guess1=input("First guess: ")
    if (guess1.lower())in(birds)==True:
        print("Correct bird! 1/3")
        quit
    else: 
        print("Incorrect bird.")
    guess2=input("Second guess: ")
    if guess2 in(birds)==True:
        print("Correct bird! 2/3")
        quit
    else:
        print("Incorrect bird.")
    guess3=input("Final guess: ")
    if guess3 in(birds)==True:
        print("Correct bird! 3/3")
        quit
    else:
        print("Incorrect bird.")
        print("Game over!")
        quit