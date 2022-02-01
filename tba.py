print("Short text based adventure game with no random variation!")
print("Copyright lolololololol by 2.5 Idiots studios")
print("Would you like to begin? [Y/N]")
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