#Will C.
#Python 1
#Unit 3, Mod 1.2

#imports
from datetime import time
from datetime import date
from datetime import datetime
#Task 1
# [ ] Create a `time` variable containing the time: 8:45 AM
t1=time(hour=8,minute=45)
# [ ] Create a `time` variable containing the time: 8:45:01:000150 PM
t2=time(hour=8,minute=45,second=1,microsecond=150)
# [ ] Print the hour (only) contained in t3 
t3 = time(hour = 15, minute = 10, second = 0) 
# [ ] Modify t3 to: 4:10 PM 
t3 = time(hour = 15, minute = 10, second =0)
h=t3.hour
print(h)

#Task 2
# [ ] Create a `date` variable containing: (March 28 2012)
d1=date(year=2012,month=3,day=28)
print(d1)
# [ ] Prompt the user to enter a month and a day, get the current year, then create a date object with the information collected
while True:
    m=input("Enter a month: ")
    if m.lower()=="january":
        m=1
        break
    elif m.lower()=="february":
        m=2
        break
    elif m.lower()=="march":
        m=3
        break
    elif m.lower()=="april":
        m=4
        break
    elif m.lower()=="may":
        m=5
        break
    elif m.lower()=="june":
        m=6
        break
    elif m.lower()=="july":
        m=7
        break
    elif m.lower()=="august":
        m=8
        break
    elif m.lower()=="september":
        m=9
        break
    elif m.lower()=="october":
        m=10
        break
    elif m.lower()=="dovember":
        m=11
        break
    elif m.lower()=="december":
        m=12
        break
    elif m.isdigit()==True:
        break
    else:
        print("Unexpected input.")
d=input("Enter a day: ")
chosenDate=date(year=2022,month=int(m),day=int(d))
print(chosenDate)

#Task 4
# [ ] Create a `datetime` variable containing: (March 28 2012 @ 12:55:10:30 AM)
dt1=datetime(year=2012,month=3,day=28,hour=12,minute=55,second=10,microsecond=30)
print(dt1)
# [ ] Write code that prints the current hour
dt2=datetime.today()
t4=dt2.time()
h1=t4.hour
print(h1)
# [ ] Write a program that prints the current date on one line and the current time on another line
dt3=datetime.today
d2=dt3.date()
# [ ] Write a program that: 
# 1) prompts the user for a time (hours and minutes only) 
# 2) gets the current date 
# 3) combines the collected information into a `datetime` variable 