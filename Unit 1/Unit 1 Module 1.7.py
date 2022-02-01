#Will C.
#Python 1
#Unit 1, mod 1.7

#Task 1
# [ ] print 3 strings on the same line using commas inside the print() function
print("There is","a comma","in this print statement.")

#Task 2
# [ ] use a print() function with comma separation to combine 2 numbers and 2 strings 
print(1,"comma",2,"commas")

#Task 3
# [ ] get user input for a street name in the variable, street
print("What is the street name?")
street=input()
# [ ] get user input for a street number in the variable, st_number
print("What is the street number?")
st_number=input()
# [ ] display a message about the street and st_number
print("The address is",st_number,street)

#Task 4
# [ ] define a variable with a string or numeric value
var=7
# [ ] display a message combining the variable, 1 or more literal strings and a number
print("Lorem ipsum",var,4)

#Task 5
# [ ] get input for variables: owner, num_people, training_time  - use descriptive prompt text 
print("Please enter the name of the leader of the training group:")
owner =  input()
print("Please enter the number of people attending:")
num_people =  input()
print("Please enter the time that your session will start at:")
training_time =  input()
# [ ] create an integer variable min_early and "hard code" the integer value (e.g. - 5, 10 or 15) 
min_early =  5
# [ ] print reminder text using all variables & add additional strings -  use comma separated print formatting
print("Your training has been scheduled by",owner,"with",num_people,"attending. The training will start at",training_time,"so please arrive",min_early,"minutes prior to your scheduled time.")