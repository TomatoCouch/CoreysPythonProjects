#Will C.
#Python 1
#Unit 3, Mod 1.3

#imports
from datetime import timedelta
from datetime import datetime
#Task 1
# [ ] Create a `timedelta` object that contains: 2 hours, 3 minutes, and 1 week 
td=timedelta(hours=2,minutes=3,weeks=1)
# [ ] Use a `timedelta` object to calculate the total number of seconds in: 1 hour and 15 minutes 
hourFifteen=timedelta(hours=1,minutes=15)
print(hourFifteen.seconds)
# Use a `timedelta` object to find out how many days are left until your upcoming birthday
bday=datetime(year=2022,month=8,day=12)
date=datetime.today()
daysTillBday=bday-date
print(daysTillBday)

#Task 2
# [ ] Write a program to compute the date 3 weeks before your birthday  
# to help you remember when to send the invitations 
threeWeeks=timedelta(weeks=3)
reminder=bday-threeWeeks
print("Birthday reminder on",reminder)
# [ ] Write a program that computes the number of days from the current date till the 3 weeks reminder 
# 1) Create a `timedelta` object (td1) for the period between the current date and your upcoming birthday
td1=bday-date
# 2) Create a `timedelta` object (td2) containing 3 weeks
td2=timedelta(weeks=3)
# 3) Use the `timedelta` objects (td) from 1 and 2 to compute the required number of days 

#Task 3
# [ ] Write a program to find out if 4th of July of this year has passed or not
fourthOfJuly=datetime(year=2022,month=7,day=4)
if date<fourthOfJuly:
    print("Still waiting.")
else:
    print("It's passed.")

#Task 4
# [ ] Complete the following program to find out if you are closer to the current year's June or December solstice 
# Define today's date 
now = datetime.today() 
# Define the December solstice 
december_solstice = datetime(month = 12, day = 21, year = now.year) 
# Define the June solstice 
june_solstice = datetime(month = 6, day = 21, year = now.year) 
# Find out which solstice is closer 
if (december_solstice-now)<(june_solstice-now):
    print("December solstice closer.")
else:
    print("June solstice closer.")