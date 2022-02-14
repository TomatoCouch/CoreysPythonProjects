#Will C.
#Python 1
#Homework assignment

#Task 1
# [ ] define and call a function short_rhyme() that prints a 2 line rhyme
def short_rhyme():
    print("This little thing, I made it rhyme")
    print("Simply by ending this line with lime")
short_rhyme
# [ ] define (def) a simple function: title_it() and call the function
# - has a string parameter: msg
# - prints msg in Title Case
def title_it(msg):
    print(msg.title())
# [ ] get user input with prompt "what is the title?"
msg=input("What is the title? ")
# [ ] call title_it() using input for the string argument
title_it(msg)
# [ ] define title_it_rtn() which returns a titled string instead of printing
def title_it_rtn(thing_to_title):
    return thing_to_title.title()
# [ ] call title_it_rtn() using input for the string argument and print the result
print(title_it_rtn(input("What would you like titled? ")))

#Task 2
# [ ] create, call and test bookstore() function
def bookstore(book,price):
    return "Title:",book.title(),"costs",price
print(bookstore(input("What book would you like? "),input("How much does it cost?")))
#Task 3
def make_greeting(name, greeting = "Hello"):
    return (greeting + " " + name + "!")
# get name and greeting, send to make_greeting
get_name=input("What is your name? ")
get_greeting=input("How would you like to be greeted? ")
print(make_greeting(get_name, get_greeting))
def get_name():
    name_entry = input("enter a name: ")
    return name_entry
def get_greeting():
    greeting_entry = input("enter a greeting: ")
    return greeting_entry
