#Will C.
#Python 1 
#Unit 1, mod 1.6

# [ ] get input for the variable student_name
from cgi import test


student_name=input()
# [ ] determine the type of student_name 
print(type(student_name))
# [ ] run cell several times, entering a name, an integer number, and a float number after adding cod
print("enter a name or number") 
test_input = input() 
# [ ] insert code below to check the type of test_input
print(type(test_input))

#Task 2
# [ ] get user input for a city name in the variable named city 
print("Enter your city's name:")
city=input()
# [ ] print the city name
print("Your city is " + city)
# [ ]create variables to store input: name, age, get_mail with prompts for name, age and yes/no to being on an email list 
# [ ] print a description + variable value for each variable 
print("What is your name?")
name=input()
print("How old are you?")
age=input()
print("Would you like to be added to our email list?")
get_mail=input()