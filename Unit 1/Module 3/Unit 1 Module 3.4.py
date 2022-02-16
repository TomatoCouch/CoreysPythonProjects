#Will C.
#Python 1
#Unit 1, mod 3.4

#Task 1
# [ ] code and test SHIRT SALE
print("Welcome to Will's Shirt Shop!")
print("All shirts sourced locally from the finest sweatshops in some 3rd world country.")
size=input("What size shirt would you like? We have small, medium, large, and extra large. ").lower()
if size=="small":
    print("A small will be $6.00.")
elif size=="sm":
    print("A small will be $6.00.")
elif size=="sml":
    print("A small will be $6.00.")
elif size=="medium":
    print("A medium will be $7.00.")
elif size=="m":
    print("A medium will be $7.00.")
elif size=="md":
    print("A medium will be $7.00.")
elif size=="large":
    print("A large will be $8.00.")
elif size=="l":
    print("A large will be $8.00.")
elif size=="lg":
    print("A large will be $8.00.")
elif size=="extra large":
    print("An extra large will be $9.00.")
elif size=="xl":
    print("An extra large will be $9.00.")
elif size=="extra-large":
    print("An extra large will be $9.00.")
else:
    print("Unexpected input.")

#Task 2
str_num_1 = "11" 
str_num_2 = "15" 
int_num_3 = 10
print(int(str_num_1)+int(str_num_2)+int_num_3)
print(str_num_1+str_num_2+str(int_num_3))
# [ ] code and test: adding using int casting 
str_integer = "2" 
int_number = 10 
number_total = int(str_integer) + int_number 
print(number_total) 

#Task 3
#With David
int1=int(input("Please input an integer (any positive or negative whole number): "))
operation=input("Please input which operation (addition, subtraction, multiplication, division) you'd like to perform: ").lower()
int2=int(input("Please input a second integer: "))
if operation=="multiply":
    print("Your product is:",int1*int2)
elif operation=="multiplication":
    print("Your product is:",int1*int2)
elif operation=="*":
    print("Your product is:",int1*int2)
elif operation=="add":
    print("Your sum is:",int1+int2)
elif operation=="addition":
    print("Your sum is:",int1+int2)
elif operation=="+":
    print("Your sum is:",int1+int2)
elif operation=="subtract":
    print("Your difference is:",int1-int2)
elif operation=="subtraction":
    print("Your difference is:",int1-int2)
elif operation=="-":
    print("Your difference is:",int1-int2)
elif operation=="divide":
    print("Your quotient is:",int1//int2)
elif operation=="division":
    print("Your quotient is:",int1//int2)
elif operation=="/":
    print("Your quotient is:",int1//int2)
else:
    print("Unknown operation.")