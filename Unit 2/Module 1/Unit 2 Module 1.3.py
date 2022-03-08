#Will C.
#Python 1
#Unit 2, Mod 1.3

#Task 1
# [ ] Get user input for first_name
first_name=input("What is your first name? ").capitalize()
# [ ] iterate through letters in first_name
for letter in first_name:
    print(letter)
#    - print each letter on a new line

#Task 2
# [ ] Create capitalize-io
first_name=input("What is your first name? ").capitalize()
new_name=""
for letter in first_name:
    if letter.lower()=="o":
        new_name+=letter.upper()
    elif letter.lower()=="i":
        new_name+=letter.upper()
    else:
        new_name+=letter
print(first_name,"to",new_name)

#Task 3
# [ ] create & print a variable, other_word, made of every other letter in long_word 
long_word = "juxtaposition"
drow_gnol=long_word[::2]
print(drow_gnol)
# Mirror Color 
# [ ] get user input, fav_color 
fav_color=input("What is your favorite color? ")
# [ ] print fav_color backwards + fav_color
print(fav_color[::-1]+fav_color)
# example: "Red" prints "deRRed"