#Degrees -> Degrees by default
from cmath import pi


print("Will's Degree/Radian calculator!")
doRad=False
doDeg=True
while True:
    if doDeg==True and doRad==False:
        num=input("Enter your degrees. To quit, enter quit. To switch conversion, enter swap. If you'd like pi to remain in your answers, enter pi.\nNOTE: Entering anything that isn't a number will cause an error. Don't do that.\n")
        if num.lower()=="quit":
            quit()
        elif num.lower()=="swap":
            doDeg=False
            doRad=True
        elif num.lower()=="pi":
            while True:
                print("no")
        else:
            print(num,"degrees is equivalent to:",float(num)*(pi/180.0),"radians.")
    elif doDeg==False and doRad==True:
        num=input("Enter your radians. To quit, enter quit. To switch conversion, enter swap. If you'd like pi to remain in your answers, enter pi.\nNOTE: Entering anything that isn't a number will cause an error. Don't do that.\n")
        if num.lower()=="quit":
            quit()
        elif num.lower()=="swap":
            doDeg=True
            doRad=False
        elif num.lower()=="pi":
            while True:
                print("no")
        else:
            print(num,"radians is equivalent to:",float(num)*(180.0/pi),"radians.")