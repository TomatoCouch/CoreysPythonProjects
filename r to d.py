#Degrees -> Degrees by default
from cmath import pi


print("Will's Degree/Radian calculator!")
doRad=False
doDeg=True
while True:
    if doDeg==True and doRad==False:
        num=input("Enter your degrees. To quit, enter quit. To switch conversion, enter swap.\n")
        if num.lower()=="quit":
            quit()
        elif num.lower()=="swap":
            doDeg=False
            doRad=True
        else:
            print(num,"degrees is equivalent to:",float(num)*(pi/180.0),"radians.")
    elif doDeg==False and doRad==True:
        num=input("Enter your radians. To quit, enter quit. To switch conversion, enter swap.\n")
        if num.lower()=="quit":
            quit()
        elif num.lower()=="swap":
            doDeg=True
            doRad=False
        else:
            print(num,"radians is equivalent to:",float(num)*(180.0/pi),"radians.")