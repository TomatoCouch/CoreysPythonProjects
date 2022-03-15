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