#Will C.
#Python 1
#Unit 3, Mod 1.1

#Task 1
# [ ] Import the math module and use an appropriate function to find the greatest common divisor of 16 and 28
import math
import random
math.gcd(16,28)
# [ ] Prompt the user to input 2 positive integers then print their greatest common divisor 
while True:
    num1=input("Input your first number: ")
    if num1.isdigit()==True:
        num1=int(num1)
        break
    else:
        print("Only numbers, please.")
while True:
    num2=input("Input your second number: ")
    if num2.isdigit()==True:
        num2=int(num2)
        break
    else:
        print("Only numbers, please.")
print(math.gcd(num1,num2))

#Task 2
# [ ] Fill out the function is_even with a code block that returns True if n is even and returns False if n is odd 
def is_even(n): 
    if n%2==0:
        return True
    else:
        return False
# Test the function  
x = 5
if is_even(x): 
    print("Number is even") 
else: 
    print("Number is odd") 
     
# [ ] Use the function is_even to print the square root of all the even numbers in the following list 
l = [25, 34, 193, 2, 81, 26, 44] 
def is_even(n): 
    return (n % 2) == 0
count=0
for item in l:
    if is_even(int(l[count]))==True:
        print(math.sqrt(l[count]))
        count=+1
    else:
        count=+1

#Task 3
# [ ] Correct the following expression so the answer is 10 
#4 + 16 / 2
(4+16)/2 

# [ ] Correct the following expression so the answer is 250; review the operator precedence table and use only one () pair 
#2 * 3 + 2 ** 3 
(2*3)+2**3

#Task 4
# [ ] Use an appropriate rounding function to round 75.34 to 75 and then to 76 
x = 75.34 
print(math.floor(x))
print(math.ceil(x))
# [ ] Use an appropriate rounding function to fix the following `float` error 
# Price of a chocolate box 
p = 4.35 
# Quantity needed 
q = 200 
# Order total price (Should be 4.35 * 200 = $870.00) 
total = p * q 
print("Total price: ", math.floor(total))

#Task 5
def die_roller (): 
    return (random.randint(1, 6))
def odd_random(): 
    return (random.randrange(1, 102, 2)) 
# [ ] Modify the die_roller() function to use randrange instead of randint
def dieRoller2():
    return (random.randrange(1,7))
# [ ] Modify the odd_random() function to use randint instead of randrange
def oddRandom2():
    return (random.randint(1,101))
# [ ] Complete the function dice_roller() so it rolls 2 dice 
# Use the die_roller function 
from random import randint 
def die_roller(): 
    return(randint(1, 6)) 
def diceRoller3(): 
    print(randint(1,6))
    print(randint(1,6))
diceRoller3()

#Task 6
def pick_card(): 
    card_type = ['Clubs', 'Diamonds', 'Hearts', 'Spades']; 
    card_number = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'] 
     
    # choose a type at random 
    t = random.choice(card_type) 
    n = random.choice(card_number) 
     
    return [n, t] 
# Show the randomly picked card 
print(pick_card()) 
# [ ] Modify the pick_card() function to use `shuffle` instead of choice 
def pickCard2():
    card_type = ['Clubs', 'Diamonds', 'Hearts', 'Spades']; 
    card_number = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'] 
    random.shuffle(card_type)
    random.shuffle(card_number)
    t=card_type[0]
    n=card_number[0]
    return [t,n]
# [ ] The following list contain the 10 most populous American cities; write code to randomly select one of the cities to visit 
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
randnum=random.randint(0,10)
print(cities[randnum])