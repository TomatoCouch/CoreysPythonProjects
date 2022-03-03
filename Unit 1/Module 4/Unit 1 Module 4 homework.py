#Will C.
#Python 1
#Unit 1, Mod 4 homework
from random import randint

#Part 1
# [ ] use a "forever" while loop to get user input of integers to add to sum,
# until a non-digit is entered, then break the loop and print sum

sum = 0
while True:
    intadd=input("Enter an integer to add. To quit, enter a non-integer. To see your number, input 'num': ")
    if intadd.isdigit()==True: 
        sum=sum+int(intadd)
    elif intadd.lower()=="num":
        print("Your number is:\n"+str(sum))
    else:
        print("Non-integer detected.\nYour number was:\n"+str(sum))
        break

#Part 2
# [ ] use a while True loop (forever loop) to give 4 chances for input of a correct color in a rainbow
# rainbow = "red orange yellow green blue indigo violet"
rainbow = "red orange yellow green blue indigo violet"
count=0
while count<4:
    guess=input("Tell me a color of the rainbow: ").lower()
    if (guess in(rainbow))==True:
        print("Correct guess!")
        count+=1
    else:
        print("Incorrect guess!")
        count+=1

#Part 3
# [ ] Get input for a book title, keep looping while input is Not in title format (title is every word capitalized)
title = ""
while title.istitle()==False:
    title=input("Enter a title in title format (every word is capitalized)")
    if title.istitle()==False:
        print("Not in title format.")
    else:
        print("In title format.")

#Part 4
# [ ] create a math quiz question and ask for the solution until the input is correct
numOne=randint(1,10)
numTwo=randint(1,10)
answer=0
while answer!=numOne*numTwo:
    print("What is",numOne,"times",numTwo)
    answer=int(input())
    if answer!=numOne*numTwo:
        print("Incorrect answer.")
    else:
        print("Correct.\n"+str(numOne),"*",str(numTwo),"=",str(answer))