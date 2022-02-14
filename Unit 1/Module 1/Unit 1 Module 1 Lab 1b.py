#Will C.
#Python 1
#Homework assignment

# [ ] get user input for a variable named remind_me
print("Add a reminder:")
remind_me=input()
# [ ] print the value of the variable remind_me 
print(remind_me)
# use string addition to print "remember: " before the remind_me input string
print("Remember:",remind_me)

#Task 2
# [ ] get user input for 2 variables: meeting_subject and meeting_time
print("What will your meeting be about?")
meeting_subject=input()
print("And what time will your meeting be?")
meeting_time=input() + "."
# [ ] use string addition to print meeting subject and time with labels
print("Your meeting about",meeting_subject,"will start at",meeting_time)

#Task 3
# [ ] print the combined strings "Wednesday is" and "in the middle of the week"
print("Wednesday is","in the middle of the week")
# [ ] print combined string "Remember to" and the string variable remind_me from input above
print("Remember to",remind_me)
# [ ] Combine 3 variables from above with multiple strings
print("Remember to",remind_me,"and don't forget your meeting about",meeting_subject,"at",meeting_time)

#Task 4? These aren't seperated with task numbers so I'm just guessing
# [ ] print a string sentence that will display an Apostrophe (')
print("'")
# [ ] print a string sentence that will display an Apostrophe (')
print("'")
#that was easy
#that's what it showed up as on the assignment llllllllllllllllllllllllL

#Task 5
# [ ] complete vehicle tests
vehicle=input("Name a vehicle:")
# [ ] print True or False if color starts with "b"
print("color".startswith("b"))

#Task 6
# [ ] get user input for a variable named color
color=input("Choose a color:")
# [ ] modify color to be all lowercase and print
print(color.lower())
# [ ] get user input using variable remind_me and format to all **lowercase** and print
remind_me=input()
print(remind_me.lower())
# [ ] test using input with mixed upper and lower cases
test=input("say something wacky with mixed upper and lower cases")
# [] get user input for the variable yell_this and format as a "YELL" to ALL CAPS
yell_this=input("What would you like to yell?")
print(yell_this.upper())