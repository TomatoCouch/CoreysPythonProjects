#The Laboratory
#Where I can tinker around

#print("Do you see this?") (to the comment realm with you, bastard)
#if input("Yes"):print("Great") (didn't work)
#if askstring(prompt="can you see this?"):print ("Great!") (no clue what i'm doing)

#how do boolean
#bool=True (commented to not print before my pipe bomb script)
#print(type(True)) (ditto)
#ok then
#are_these_case_sensitive=True (commented to not print before my pipe bomb script)
#print(are_these_case_sensitive) (ditto)

#now for The Funny(tm)
#is_there_a_pipe_bomb_in_your_mailbox=True
#print("Let's see if there's a pipe bomb in your mailbox.")
#print("In order to do so, we'll check the boolean is_there_a_pipe_bomb_in_your_mailbox.")
#print("The boolean is:")
#print(is_there_a_pipe_bomb_in_your_mailbox)
#if(is_there_a_pipe_bomb_in_your_mailbox==True): 
#    print("Run."), 
#else: print("You're safe, for now.") (commented so I could keep going)

#print("What is your name?")
#name=input()
#if name=="Elon Musk":
#    print("There is an IED on your porch.")
#else: print("You may live.")

#def fishstore(fish, price = "1"):
#    sentence = "Fish Type: " + fish + " costs $" + price
#    return sentence
#fish_entry = input("Enter fish name: ")
#price_entry = input("Enter the fish price (no symbols): ")

#print(fishstore(fish_entry, price_entry))

#Official bitch counter
#name = input("What is your name? ").lower()
#if name=="aiden":
#    print("You have zero (0) bitches.")
#else:
#    print("You have an unknown amount of bitches.")

#Super fun true or false incredible ultra difficult quiz made entirely in python!
print("Super fun true or false incredible ultra difficult quiz made entirely in python!")
print("By Will")
yesStart=False
while yesStart==False:
    start=input("Would you like to begin? ")
    if start=="yes":
        print("Great!")
        yesStart=True
    elif start=="no":
        print("Ok")
        quit()
    else:
        print("I don't understand your response.")

print("Question 1:")
print("The CIA took part in an experiment called MKUltra where they tested drugs abilities to enhance human abilities. During this, a few people died, one of which was an agent who expressed dissent towards the experiment. He was secretly injected with LSD leading to his suicide.")
print('(Please input your answer as "True" or "False"')
q1Answer=input("True or False? ").lower()
if q1Answer=="true":
    print("Correct.")
    q1Correct=True
else:
    print("Incorrect.")
    q1Correct=False
