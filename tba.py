print("Short text based adventure game with no random variation!")
print("Copyright lolololololol by 2.5 Idiots studios.")
print("Since I couldn't be bothered to essentially duplicate my code, please input all commands entirely in lowercase.")
print("Would you like to begin? [y/n]")
begin=input()
if begin=="y":
    game_start="yes"
elif begin=="n":
    print("Ok")
    quit()
else:
    print("Please use 'Y' or 'N' to select a choice.")
    game_start=input()
if game_start=="yes":
    print("You find yourself locked in a dark room. The ground is cold, and you feel things in your pockets. What do you do?")
action=input()
if action=="stand up":
    print("You slowly climb to your feet, touching the ground in the process. It's smooth and uneven. What do you do?")
