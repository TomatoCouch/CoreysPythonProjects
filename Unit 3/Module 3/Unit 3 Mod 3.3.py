#Will C.
#Python 1
#Unit 3, Mod 3.3

#Imports
from datetime import datetime


#Task 1
# [ ] Create a tuple that consists of the following variables
x = 5
l = [4.4, 5.3]
s = "something"
t = (9, 0)
firstTuple=(x,l,s,t)
# [ ] Change the third element of T to [59, 20.4] 
T = ([43.6, 34], [49, 59], [50, 34.6], [39, 49])
print(T)
T = ([43.6, 34], [49, 59], [59, 20.4], [39, 49])
print(T)
# [ ] Write a program to merge the content of T1 and T2 into one tuple T 
# Correct output should be T = (5, 4, 3, 9, 2, 12) 
# T = ((5, 4, 3), (9, 2, 12)) is an incorrect output 
# Hint: Use list to/from tuple conversion 
T1 = (5, 4, 3) 
T2 = (9, 2, 12)
T=list(T1)+list(T2)
T=tuple(T)
print(T)

#Task 2
# [ ] Write a program to split the content of T into T1 and T2
# T1 = (5, 4, 3)
# T2 = (9, 2, 12)
T = (5, 4, 3, 9, 2, 12)
T1=list(T[0:3])
T2=list(T[3:6])
print("T1 =",T1)
print("T2 =",T2)
# [ ] Write an expression to unpack `T` into:
# 1) x = 5
# 2) l = [3, 5.3]
# 3) s = 'something
# 4) t = (9, 0)
T = (5, [3, 5.3], 'something', (9, 0))
#TODO: Your code goes here
x=T[0]
l=T[1]
s=T[2]
t=T[3]
print("After unpacking the tuple:", T)
print("x =", x)
print("l =", l)
print("s =", s)
print("t =", t)
# [ ] Complete the function `current_date` to return today's month, day, and year 
# Hint: Use an appropriate function from the datetime module 
def current_date(): 
    dateAndTime=datetime.now()
    mmddyyyy=(dateAndTime.month,dateAndTime.day,dateAndTime.year)
    return mmddyyyy
m, d, y = current_date() 
print("Today's date is: {:2d}/{:2d}/{:4d}".format(m, d, y))

#Task 3
# [ ] Write a program to merge the content of T1 and T2 into one tuple T 
# Correct output should be T = (5, 4, 3, 9, 2, 12),  
# T = ((5, 4, 3), (9, 2, 12)) is an incorrect output 
# You should NOT use lists in your solution 
T1 = (5, 4, 3) 
T2 = (9, 2, 12)
T=T1+T2
print(T)
# [ ] Write a program to prompt the user for a number, then test if the number is contained in T 
T = (23, 45, 93, 59, 35, 58, 19, 3)
guess=input("Guess a number: ")
if int(guess) in T:
    print("Congratulations! You guessed correctly!")
else:
    print("Uh oh! You guessed incorrectly!")
# Write a function to return the largest element in a tuple T 
T = (23, 45, 93, 59, 35, 58, 19, 3)
T=sorted(T)
print(T[-1])
# [ ] Write a program to compute the average of the elements in T 
T = (23, 45, 93, 59, 35, 58, 19, 3) 
sum=0
for num in T:
    sum=sum+num
print(sum/len(T))