#Do I need to like, do something before this?
#Traceback (most recent call last):
#  File "c:\Users\Harry\Documents\GitHub\WillsPythonProjects\turtle.py", line 2, in <module>
#    import turtle
#  File "c:\Users\Harry\Documents\GitHub\WillsPythonProjects\turtle.py", line 4, in <module>
#    s = turtle.getscreen()
#AttributeError: partially initialized module 'turtle' has no attribute 'getscreen' (most likely due to a circular import)
#what
#maybe if i didn't make the file name and library name as the same thing, this would've worked first time???
#god i'm stupid
import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)