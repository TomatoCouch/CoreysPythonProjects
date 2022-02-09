#Will C.
#Python 1
#Unit 1, mod 2.2

#Task 1
# create and call make_doctor() with full_name argument from user input - then print the return value
def make_doctor(name):
    dr_name = "Dr. " + name
    return dr_name
doctors_name=input("What is your name?")
print("You are",make_doctor(doctors_name))

#Task 2
#def make_schedule(period1, period2): 
#    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title()) 
#    return schedule 
#student_schedule = make_schedule("mathematics", "history") 
#print("SCHEDULE:", student_schedule) 
# [ ] add a 3rd period parameter to make_schedule
def make_schedule(period1, period2, period3): 
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] ", period3.title())
    return schedule 
student_schedule = make_schedule("mathematics", "history", "science") 
print("SCHEDULE:", student_schedule) 