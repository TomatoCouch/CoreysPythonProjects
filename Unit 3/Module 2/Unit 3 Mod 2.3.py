#Will C.
#Python 1
#Unit 3, Mod 2.3

# [ ] Write a program to prompt the user for an integer input between 0 and 100
# then print if the number is contained in `lst`
lst = [22, 89, 69, 78, 58, 22, 56, 13, 74, 8, 32, 58, 8, 63, 46, 79, 9, 38, 25, 96]
while True:
    guess=int(input("Enter a number between 0 and 100. "))
    if guess>100:
        print("Number greater than 100.")
    elif guess<0:
        print("Number less than 0.")
    elif guess in lst:
        print("Number is in list.")
        break
    elif guess not in lst:
        print("Number is not in list.")
    else:
        print("How did you activate this condition")
# [ ] The `records` list contains information about a company's employees
# each of the elements in `records` is a list containing the name and ID of an employee.
# Write a program to test if `applicant` is contained in `records` and display an appropriate message
# Records of names and IDs
records = [['Colette', 22347], ['Skye', 35803], ['Alton', 45825], ['Jin', 24213]]
applicant = ['Joana', 20294]
if applicant in records:
    print("Name already exists in registry.")
else:
    print("Name does not exist in registry.")
# [ ] Write a program to prompt the user for a letter (capital or small) then print if the letter is a vowel
# HINT: Use a string containing all the vowels and the `in` or `not in` operator
while True:
    letter=input("Enter a letter.")
    if len(letter)>1:
        print("One letter only, please.")
    elif letter.isalpha()==False:
        print("A letter, please.")
    else:
        if letter in "aeiouAEIOU":
            print("Letter is a vowel.")
            break
        elif letter=="y":
            print("Letter is 'y'.")
            break
        else:
            print("Letter is not a vowel.")
            break
