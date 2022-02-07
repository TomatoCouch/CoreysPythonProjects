#Will C.
#Python 1
#Unit 1, mod 1.9

#Task 1
# [ ] get input for a variable, fav_food, that describes a favorite food 
fav_food=input("What is your favorite food? ")
# [ ] display fav_food as ALL CAPS, used in a sentence
print("So you love",fav_food.upper() + ",","correct?")
# [ ] display fav_food as all lower case, used in a sentence
print("Well if you love",fav_food.lower() + ",","why don't you marry it?")
# [] display fav_food with swapped case, used in a sentence 
print("What about",fav_food.swapcase() + "?")
# [] display fav_food with capitalization, used in a sentence
print(fav_food.capitalize(),"really must be your favorite food.")

#Task 2
# [] input variable fav_color as upper
fav_color=input("What is your favorite color?").upper()
# [] print fav_color
print(fav_color)

#Task 4
# [] print 3 tests, with description text, testing the menu variable for 'pizza', 'soup' and 'dessert
menu = "salad, pasta, sandwich, pizza, drinks, dessert" 
print("pizza in menu =",'pizza' in menu)
print("soup in menu =",'soup' in menu)
print("dessert in menu =",'dessert' in menu)
# Create a program where the user supplies input to search the menu
menu_ask=input("What would you like to check for? ").lower()
print(menu_ask,"availability =", menu_ask in menu)
#Tried to if else this task but I couldn't figure it out