#Will C.
#Python 1
#Unit 1, mod 2.1

#Task 1
#[ ] increase the number of arguments used in print() to 8 or more  
student_age = 17 
student_name = "Hiroto Yamaguchi" 
class_start = "February 3rd" + "."
print(student_name,'will be in the class for',student_age, 'year old students.', 'please welcome him on',class_start,"Please ensure he has a great class." )

#Task 2
#[ ] define (def) a simple function called yell_it() and call the function
def yell_it():
    print("i'm yelling".upper())
yell_it()

#Task 3
# [ ] define yell_this()
def yell_this(phrase):
    print(phrase.upper())
# [ ] get user input in variable words_to_yell 
words_to_yell=input("What words would you like to yell? ")
# [ ] call yell_this function with words_to_yell as argument
yell_this(words_to_yell)