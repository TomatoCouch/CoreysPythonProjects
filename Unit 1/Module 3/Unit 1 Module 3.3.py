#Will C.
#Python 1
#Unit 1, mod 3.3

#Task 1
msg = "Hello" 
# [ ] print the True/False results of testing if msg string equals "Hello" string 
print(msg=="Hello")
greeting = "Hello" 
# [ ] get input for variable named msg, and ask user to 'Say "Hello"' 
msg = input('Say "Hello"! ')
# [ ] print the results of testing if msg string equals greeting string 
print(msg=="Hello")

#Task 2
# [ ] get input for a variable, answer, and ask user 'What is 8 + 13? : ' 
answer=input("What is 8 + 13? ").lower()
# [ ] print messages for correct answer "21" or incorrect answer using if/else 
if answer=="21":
    print("Correct.")
elif answer=="twenty one":
    print("Correct.")
elif answer=="twenty-one":
    print("Correct.")
else:
    print("Incorrect.")
# note: input returns a "string"

#Task 3
#With Jose
# [ ] Create the program, run tests 
def tf_quiz(question, correct_ans):
    print(question)
    ans=input("True or false? ").lower()
    if correct_ans==ans:
        print("Correct.")
    else:
        print("Incorrect.")
print(tf_quiz("Do pigs fly?","false"))