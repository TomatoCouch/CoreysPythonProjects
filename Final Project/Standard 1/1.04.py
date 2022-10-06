#Will C.
#Python 1
#Final Project, Standard 1.04

#Standard 1.04: Nesting and Loops
#in my attempt to prove my knowledge
#i learned i have none
#why did this not work at first
#i hate vscode
while True:
    feedback=input("Enter anything: ")
    if feedback.isalnum()==True:
        print("Is alnum = True")
        if feedback.isalpha()==True:
            print("Is alpha = True")
            if feedback=="True" or feedback=="False":
                print("Input is bool = True")
                print("You entered a boolean!")
            else:
                print("Input is string = True")
                print("You entered a string!")
    elif feedback.isdigit()==True:
        print("Input is digit = True")
        print("You entered an integer!")
    elif "." in feedback:
        print(". in feedback = True")
        print("You entered a float!")
    else:
        print("Exception")