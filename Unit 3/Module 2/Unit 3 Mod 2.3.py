#Will C.
#Python 1
#Unit 3, Mod 2.3

#Task 1
# [ ] The following program tests if `num` is prime or not, use a `break` statement to improve its efficiency
# and reduce the number of necessary iterations
# Compare the number of necessary iterations with and without the `break` statement
# Use the following numbers for the comparison:
num = 45345
#num = 11579
#num = 948240
#num = 128093
#num = 519937
#num = 694394
prime = True # assume num is prime unless proven otherwise
iteration_count = 0
for i in range(2, num):
    if num % i == 0:
        prime = False;
        iteration_count = iteration_count + 1
# Display results
if prime:
    print(num, "is prime")
else:
    print(num, "is NOT prime")
    print("Total number of iterations:", iteration_count)
# [ ] Write a program to prompt the user for an odd number; use an infinite loop and a `break` statement.
while True:
    number=int(input("Please enter an odd number. "))
    if num%2==1:
        print("Number is:\nOdd\nThank you for your time.")
        break
    else:
        print("Number is:\nEven\nPlease try again.")
# [ ] Modify the following program to display numbers that are divisible by 7 along with their square roots.
# HINT: Use a `continue` statement in the loop
from math import sqrt
for num in range(1, 100):
#TODO
    if num%7!=0:
        continue
    print(num," ",sqrt(num))

#Task 2
# [ ] Write a program to display the sum of each row in table
table = [[5, 2, 6], [4, 6, 0], [9, 1, 8], [7, 3, 8]]

for row in table:
    sum=0
    for col in row:
        sum=sum+col
# [ ] Complete the function `generate_star` so it displays a star of variable `size` using "*"
# For size = 5 the star should look like:
# *   *
#  * *
#   *
#  * *
# *   *
def generate_star(size):
    for row in range(size):
            for col in range(size):
                if(row==col):
                    print("*",end="")
                elif(row==size-col-1):
                    print("*", end="")
                else:
                    print(" ",end="")
            print()
# Display star
generate_star(1000)

#Task 3
# [ ] Complete the following program to count the number of even positive numbers, odd negative numbers, and zeros in `lst`
lst = [9, 0, -2, -4, -5, 2, -15, 6, -65, -7]
even_positives = 0
odd_negatives = 0
zeros = 0
for num in lst:
    if num>0 and num%2==0:
        even_positives+=1
    elif num<0 and num%2!=0:
        odd_negatives+=1
    elif num==0:
        zeros=+1
    else:
        pass
print("Number of even positives:", even_positives)
print("Number of odd negatives:", odd_negatives)
print("Number of zeros:", zeros)
# [ ] Write a program to count the number of punctuation marks (. , ? ! ' " : ;) in `s`
s = "Once you eliminate the impossible, whatever remains, no matter how improbable, must be the truth." 
punctuationCount=0
for char in s:
    if (char=='.') or (char==',') or (char=='?') or (char=='!') or (char=='\'') or (char=='"') or (char==':') or (char==';'):
        punctuationCount+1
print("Number of punctuation marks: \n"+str(punctuationCount))
# [ ] Write a program to prompt the user for an odd positive number; use an infinite loop and a `break` statement.
while True:
    number=int(input("Please enter an odd number. "))
    if num%2==1 and num>0:
        print("Number is:\nOdd\nPositive\nThank you for your time.")
        break
    elif num%2==0 and num<0:
        print("Number is:\nEven\nNegative\nPlease try again.")
    elif num%2==1 and num<0:
        print("Number is:\nOdd\nNegative\nPlease try again.")
    elif num%2==0 and num>0:
        print("Number is:\nEven\nNegative\nPlease try again.")