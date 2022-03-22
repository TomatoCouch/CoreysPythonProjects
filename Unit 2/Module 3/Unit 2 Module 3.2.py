#Will C.
#Python 1
#Unit 2, Mod 3.2

#Task 1
# [ ] for x = 6, use range(x) to print the numbers 1 through 6 
x = 6 
for num in range(x):
    print(num+1)
# [ ] using range(x) multiply the numbers 1 through 7 
# 1x2x3x4x5x6x7 = 5040
x=7
subtotal=1
for num in range(x):
    subtotal=subtotal*(num+1)
    print(subtotal)
#Use range(stop) to print the second half of spell_list below
# [ ] print the second half of a spelling list using a range(stop) loop to iterate the list 
spell_list = ["Wednesday", "Tuesday", "February", "November", "Annual", "Calendar", "Solstice"] 
half1=int(len(spell_list)/2)
for item in range(half1):
    print(spell_list[item])

#Task 2
# [ ] using range(start,stop), .append() the numbers 5 to 15 to the list: five_fifteen
five_fifteen=[]
for num in range (5,16):
    five_fifteen.append(num)
print(five_fifteen)
# [ ] print list five_fifteen 
# [ ] using range(start,stop) - print the 3rd, 4th and 5th words in spell_list 
# output should include "February", "November", "Annual" 
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"] 
for word in range(2,5):
    print(spell_list[word])
# [ ] using code find the index of "Annual" in spell_list 
# [ ] using range, print the spell_list including "Annual" to end of list 
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
annualIndex=spell_list.index("Annual")
print(spell_list[:(annualIndex+1)])

#Task 3
# [ ] print numbers 10 to 20 by 2's using range
x=10
for num in range(x,2):
    print(num)
# [ ] print numbers 20 to 10 using range (need to countdown) 
for num in range (x,-2):
    print(num)
# Hint: start at 20 
# [ ] print first and every third word in spell_list 
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
for iem in range (0, len(spell_list),3):
    print(spell_list[item])

#Task 4
#Input a word string (word)
#Find the string length of word
#use range() to iterate through each letter in word (can use to range loops)
#Save odd and even letters from the word as lists
#odd_letters: starting at index 0,2,...
#even_letters: starting at index 1,3,...
#Print odd and even lists
# [ ] complete List of letters program- test with the word "complexity"
word=input("Enter a word: ")
wordLen=len(word)
odd=[]
even=[]
for letter in range(0,wordLen):
    if letter % 2==0:
        even.append(word[letter])
    else:
        odd.append(word[letter])
print(odd)
print(even)

#Task 5
# [ ] fix the error printing odd numbers 1 - 9 
#for num in range[1,10,2]: 
#    print(num)
for num in range(1,10,2):
    print(num)