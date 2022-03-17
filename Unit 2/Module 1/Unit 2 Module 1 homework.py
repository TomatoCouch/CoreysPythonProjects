#Will C.
#Python 1
#Unit 2, Mod 1 homework

#Task 1
# [ ] access and print the second character from planet_name: "u" 
planet_name = "Jupiter" 
# [ ] access and print the first character from planet_name: "J" 
planet_name = "Jupiter" 
# [ ] access and print the first and last characters from planet_name 
planet_name = "Jupiter" 
# [ ] using a negative index access and print the first character from planet_name: "J" 
planet_name = "Jupiter" 
print(planet_name[1])
print(planet_name[0])
print(planet_name[0],planet_name[-1])
print(planet_name[-7])

#Task 2
# [ ] print planet_name sliced into the first 3 characters and remaining characters 
planet_name = "Neptune"
print(planet_name[0:3],'\n'+planet_name[3:])
# [ ] print 1st char and then every 3rd char of wise_words 
# use string slice with a step
wise_words = 'Play it who opens'
print(wise_words[0::3]) 
# [ ] print planet_name in reverse
print(planet_name[-1])
# [ ] find the number of 0's in the first half (slice) of work_tip 
# [ ] print a substring of code_tip set start index = 13 and end index = 25

#Task 3
# [ ] Get user input for 1 fav_food
fav_food=input('What is your favorite food? ')
# [ ] iterate through letters in fav_food
#    - print each letter on a new line
counter=0
while True:
    if counter==len(fav_food):
        break
    else:
        print(fav_food[counter])
        counter+=1
# [ ] iterate work_tip string concatenate each letter to variable: new_string  
# [ ] concatenate the letter or a "-" instead of a space " " 
# tip: concatenate string example: word = word + "a"
work_tip = "Good code is commented code"
blst=""
counter=0
while True:
    if counter==len(work_tip):
        break
    else:
        new_string=blst+work_tip[counter]
        counter+=1
# [ ] Print the first 4 letters of name on new line 
name = "Hiroto"
counter=0
while counter!=4:
    print(name[counter])
    counter+=1
# [ ] Print every other letter from 2nd to last letter of name  
name = "Hiroto"
print(name[2::2])

#Task 4
#Get user input for first_name
#Create an empty string variable: new_name
#Iterate through letters in first_name Backwards
#Add each letter to new_name as you iterate
#Replace the letter if "e", "t" or "a" with "?" (hint: if, elif, elif, else)
#Print new_name
# [ ] Create Mystery Name 
first_name=input("What is your first name? ")
new_name=""
counter=0
while counter!=len(first_name):
    print("loop works")
    if first_name.lower()[-(counter)]=='e':
        new_name+="?"
    elif first_name.lower()[-(counter)]=='t':
        new_name+="?"
    elif first_name.lower()[-(counter)]=='a':
        new_name+="?"
    else:
        new_name+=first_name[-(counter)]
    counter+=1
print(new_name)

#Task 5
# [ ] find and display the length of the string: topic 
topic = ".find() returns the length of a string"
print(len(topic))
# [ ] use len() to find and display the mid_pt (middle) index (+/- 1) of the string: topic
# note: index values are whole numbers 
topic = "len() can take a sequence, like a string, as an argument"
print(topic[(len(topic)//2)])
# [ ] print index where first instance of the word  "code" starts using .find() 
work_tip = "Good code is commented code"
print(work_tip.find("code"))
# [ ] search for "code" in code_tip using .find()
# [ ] search substring with substring index start= 13,end = last char  
# [ ] save result in varible: code_index 
# [ ] display index of where "code" is found, or print "not found" if code_index == -1 
work_tip = "Good code is commented code" 

#Task 6
# [ ] find and report (print) number of w's, o's + use of word "code" 
work_tip = "Good code is commented code"
print("Number of 'w's:\t\t",work_tip.find("w"))
print("Number of 'o's:\t\t",work_tip.find("o"))
print("Number of 'code's:\t",work_tip.find("code"))
# [ ]  count times letter "i" appears in code_tip string 
# [ ] find and display the index of all the letter i's in code_tip 
# Remember: if .find("i") has No Match, -1 is returned 
code_tip = "code a conditional decision like you would say it" 
print ("code_tip:" , code_tip)
print(code_tip.count('i'))
print(code_tip.find('i'))

#Task 7
#Create a program that inputs a quote (a sentence without punctuation) and prints all of the words that start with
#h-z.
#Split the words by building a placeholder variable: word, and adding a letter each loop until a non-alpha char
#is encountered
#if non-alpha detected (space, punctuation, digit,...) defines the end of a word
#else, check if word is greater than "g" alphabetically, print word and set word = empty string
#or else set word = empty string and build the next word
#Hint: use  .lower() .
# [] create words after "G" 
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
quote='"Wheresoever you go, go with all your heart"'
print('"Wheresoever you with your heart"')