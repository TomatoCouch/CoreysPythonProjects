#Will C.
#Python 1
#Unit 3, Mod 3.1

#Imports
from list import lst

#Task 1
# [ ] Complete the following program to validate a user input is outside the ranges [-50, 0] and [100, 200].
# The range limits (-50, 0, 100, 200) are not valid inputs
# Valid test inputs include: -55, 20, 99
# Invalid test inputs include: -30, 150 (and the range limts -50, 0, 100, 200)
# User input
x = input("Enter a number outside the ranges [-50, 0] and [100, 200]: ")
# convert x to int
x = int(x)
# Test input validity
if (x<-50 or x>0)==True and (x>100 or x<200)==True:
    print("True")
else:
    print("False")
# [ ] Repeat the previous task using a different conditional statement (solve it a different way)
# Complete the following program to validate a user input is outside the ranges [-50, 0] and [100, 200].
# The range limits (-50, 0, 100, 200) are not valid inputs
# User input
x = input("Enter a number outside the ranges [-50, 0] and [100, 200]: ")
# convert x to int
x = int(x)
# Test input validity 
if x<-50:
    if x>0:
        if x<100:
            if x>200:
                print("True")
            else:
                print("False")
        else:
            print("False")
    else:
        print("False")
else:
    print("False")
# [ ] Complete the following program to validate a user input is *odd* and outside the ranges [-50, 0] and [100, 200].
# The range limits (-50, 0, 100, 200) are not valid inputs
# [ ] Complete the following program to validate a user input is divisible by 3 and 
# inside either the range [-75, -25] or the range [50, 75]
# The range limit (75) is a valid input; whereas, (-50, -25, 50) are not (as they are not evenly divisible by 3)
# Valid test inputs include: -33, -60, 63
# Invalid test inputs include: -6, 33 (out of range), -29, 55 (not evanly divisible by 3)
x=input("Enter an odd number outside the ranges [-50, 0] and [100, 200]: ")
x=int(x)
if x%2==1:
    if (x<-50 or x>0)==True and (x>100 or x<200)==True:
        print("True")
    else:
        print("False")
else:
    print("False")

# [ ] The following program prompts the user for a taxable income then displays the owed taxes.
# Complete the function `tax_owed(income)` using conditional statements and the values in the tax table above.
# Test cases:
# income = 5000,   Taxes owed = $ 500.0
# income = 10000,  Taxes owed = $ 1033.75
# income = 40000,  Taxes owed = $ 5738.75
# income = 100000, Taxes owed = $ 20981.75
# income = 200000, Taxes owed = $ 49399.25
# income = 417000, Taxes owed = $ 121015.25 
# income = 500000, Taxes owed = $ 153818.85
def tax_owed(income):
    """
    Calculate the taxes owed using the tax bracket table.
    
    args:
        income: Taxable income in dollars
        
    returns:
        tax_owed: Taxes owed based on income and tax bracket
    """
    if income<5000:
        tax_owed=500.0
    elif income>5000 and income<10000:
        tax_owed=1033.75
    elif income>40000 and income<100000:
        tax_owed=5738.75
    elif income>100000 and income<200000:
        tax_owed=49399.25
    elif income>200000 and income<417000:
        tax_owed=121015.25
    elif income>417000:
        print("How do you have this much money")
    return tax_owed
# Prompt for taxable income
x = int(input("Enter the taxable income: "))
tax = tax_owed(x)
print("Taxes owed = $", tax)

# Task 2
# [ ] The following program checks if `lst` is symmetric around its center.
# In other words, it tests if the first element equals the last, the second equals the second from last, and so on.
#
# `lst` contains 10001 numbers, it was created using a symmetric list then changing the first number to 0 to break the symmetry.
# In the current form of the program, the loop needs to iterate 5000 times to complete the check regardless of the content of lst.
#
# Modify the program to improve its efficiency and reduce the number of iteration (hint- read the title)

iteration_count = 0
symmetric = True
center = len(lst) // 2; # int division (//) is used to avoid fractions for odd len(lst)
for i in range(center):
    if lst[i] != lst[len(lst) - i - 1]:
        symmetric = False
iteration_count = iteration_count + 1
print("Number of iterations:", iteration_count)
if symmetric:
    print("The list is symmetric")
else:
    print("The list is NOT symmetric")
# [ ] A palindrome is a sequence of characters which reads the same forward or backward.
# Complete the function `is_palindrome` to test if the input string `word` is a palindrome
def is_palindrome(word):
    """
    Test if word is a palindrome.
    
    Input:
    word: string to be tested
    
    Returns:
    palindrome: Boolean variable containing True if word is a palindrome, False otherwise 
    """
    backWords=word[:-1]+word[-1]
    if word.lower()==backWords.lower():
        palindrome=True
    else:
        palindrome=False
    return palindrome

# Test cases
w = "mAdam"
#w = "sir"
if (is_palindrome(w)):
    print(w.lower(), "is a palindrome")
else:
    print(w.lower(), "is NOT a palindrome")

# [ ] Write a program to prompt the user for an input outside the ranges [-50, 0] and [100, 200].
# If the user input is invalid, the program prompt the user again for a valid input.
# The range limits (-50, 0, 100, 200) are not valid inputs
while True:
    numChoice=int(input("Enter a number outside the ranges [-50, 0,] and [100, 200] "))
    if numChoice<-50:
        break
    elif numChoice>0:
        if numChoice<100:
            break
        elif numChoice>200:
            break
        else:
            pass
    elif numChoice<100:
        if numChoice>0:
            break
        elif numChoice<-50:
            break
        else:
            pass

#Task 4
# [ ] Write a program to prompt the user for an input from a predefined numerical list `valid_nums`
# If the user input is invalid, the program prompts the user again for a valid input.
valid_nums = [1, 2, 8, 16, 32, 64]
num=int(input("Enter a valid number. "))
while num not in valid_nums:
    num=int(input("Enter a valid number. "))
# [ ] The `records` list contains information about some company's employees
# each of the elements in `records` is a list containing the name and ID of an employee.
# Write a program that prompts the user for a name and return the ID of the employee if a record is found
records = [['Colette', 22347], ['Skye', 35803], ['Alton', 45825], ['Jin', 24213]]
name=input("Enter employee name. ")
if name.lower()=="colette":
    print(22347)
elif name.lower()=="skye":
    print(35803)
elif name.lower()=="alton":
    print(45825)
elif name.lower()=="jin":
    print(24213)
else:
    print("Employee not found.")
# [ ] Complete the `vowel_counter` function below so it returns the number of vowels (a, e, i, o, u) in `sentence`
vowels=["a","e",'i','o','u']
def vowel_counter(sentence):
    vowelCount=0
    for char in sentence:
        if char.lower() in vowels:
            vowelCount=+1
        else:
            pass
    return vowelCount
sentenceInput=input("Enter a sentence. ")
print(vowel_counter(sentenceInput))