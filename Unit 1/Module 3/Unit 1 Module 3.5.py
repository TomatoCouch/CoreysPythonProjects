#Will C.
#Python 1
#Unit 1, mod 3.5

#Task 1
# [ ] print the result of subtracting 15 from 43 


print(15-43)
# [ ] print the result of multiplying 15 and 43 
print(15*43)
# [ ] print the result of dividing 156 by 12 
print(156/12)
# [ ] print the result of dividing 21 by 0.5 
print(21/0.5)
# [ ] print the result of adding 111 plus 84 and then subtracting 45 
print(111+84-45)
# [ ] print the result of adding 21 and 4 and then multiplying that sum by 4 
print(21+4*4)

#Task 2
# [ ] create and test multiply() function 
def multiply(factor1,factor2):
    answer=factor1*factor2
    return answer
factor1=input("Please enter factor 1. ")
factor2=input("Please enter factor 2. ")
if factor1.isdigit()==True:
    fac1dig=True
else:
    print("Error: Factor 1 isn't a digit.")
    quit
if factor2.isdigit()==True:
    fac2dig=True
else:
    print("Error: Factor 2 isn't a digit.")
    quit
if fac1dig and fac2dig==True:
    print(str(multiply(int(factor1),int(factor2))))
else:
    print("Unexpected error.")
    quit
#that one took a lot of troubleshooting and trial and error, lots of error

#Task 4
# [ ] create improved multiply() function and test with /, no argument, and an invalid operator ($)
#def improved_multiply(number1,operator,number2):
#    if operator=="/":
#        answer2=int(number1)//int(number2)
#    elif operator.lower()=="divide":
#        answer2=int(number1)//int(number2)
#    elif operator=="*":
#        answer2=int(number1)*int(number2)
#    elif operator.lower=="multiply":
#        answer2=int(number1)*int(number2)
#    else:
#        print("Error: Invalid operator.")
#        quit
#    print(answer2)
#number1=input("Please enter number 1. ")
#operator=input("Would you like to divide or multiply? ")
#number2=input("Please enter number 2. ")
#improved_multiply(number1,operator,number2)

#Actual task 4
def improved_multiply2(number12,number22):
    product=int(number12)*int(number22)
    quotient=int(number12)/int(number22)
    print("The product of those two numbers is:",str(product))
    print("The quotient of those two numbers is:",str(quotient))
number12=input("Please input your first number: ")
number22=input("Please input your second number: ")
improved_multiply2(number12,number22)