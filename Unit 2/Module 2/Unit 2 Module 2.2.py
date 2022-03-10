#Will C.
#Python 1
#Unit 2, Mod 2.2
from random import randint

#Task 1
# Currency Values 
# [ ] create a list of 3 or more currency denomination values, cur_values
cur_values=[1,5,10,20,50]
# cur_values, contains values of coins and paper bills (.01, .05, etc.) 
# [ ] print the list 
print(cur_values)
# [ ] append an item to the list and print the list 
cur_values.append(.01)
print(cur_values)
# Currency Names 
# [ ] create a list of 3 or more currency denomination NAMES, cur_names
cur_names=["dollar","penny","nickel","dime","quarter","half-dollar"]
# cur_names contains the NAMES of coins and paper bills (penny, etc.) 
# [ ] print the list
print(cur_names)
# [ ] append an item to the list and print the list
cur_names.append("dollar coin")
print(cur_names)

#Task 2
# [ ] append additional values to the Currency Names list using input() 
cur_names.append(input("Enter a currency name: "))
# [ ] print the appended list
print(cur_names)

#Task 3
#define an empty list:  bday_survey
#get user input,  bday , asking for the day of the month they were born (1-31) or "q" to finish
#using a  while  loop
#get user input,  bday , asking for the day of the month they were born (1-31) or "q" to finish
#append the  bday  input to the  bday_survey  list
#repeat input until a user enters "q" to quit
#print bday_survey list
# [ ] complete the Birthday Survey task above
bday_survey=[]
bday=""
while bday.lower()!="q":
    bday=input("Input the day of the month you were born, or input 'q' to quit: ")
    bday_survey.append(bday)
print(bday_survey)

#Task 4
# [ ] Fix the Error 
#three_numbers = [1, 1, 2] 
#print("an item in the list is: ", three_numbers[3])
#counted index starting at 1, not 0
three_numbers = [1, 1, 2] 
print("an item in the list is: ", three_numbers[randint(0,2)])