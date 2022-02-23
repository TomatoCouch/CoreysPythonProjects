#Will C.
#Python 1
#Unit 1, mod 3.?
#this code is broken and i don't get it

def classSchedule(student_name,class_period,subject):
    schedule=student_name + "'s scheduled class for period", class_period, "is", subject
    return schedule
student_name=input("What is the student's name? ").title()
class_period=input("What is the period? ")
subject=input("What is the class subject? ").lower()
print(classSchedule(student_name,class_period,subject))
