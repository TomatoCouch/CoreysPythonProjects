#Will C.
#Python 1
#Unit 1, mod 3.2

#Task 1
X = 9 + 4 
# [ ] create a test to print() True or False for x is equal to 13 
if X==13:
    print("True")
else:
    print("False")
# [ ] create a test to print True or False for 3 + 3 is greater than 2 + 4 
if 3 + 3 > 2 + 4:
    print("True")
else:
    print("False")

#Task 2
# [ ] create an if/else statement that tests if y is greater than or equal x + x  
# [ ] print output: "y greater than or equal x + x is" True/False ...or a similar output 
x = 3 
y = x + 8
if y>=x+x:
    print("Y greater than or equal x + x is True")
else:
    print("Y greater than or equal x + x is False")
import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)