#Will C.
#Python 1
#Unit 2, Mod 1.2

#Task 1
# [ ] slice long_word to print "act" and to print "tic" 
long_word = "characteristics"
print(long_word[4:7])
print(long_word[11:14])
# [ ] slice long_word to print "sequence" 
long_word = "Consequences"
print(long_word[3:-1])

#Task 2
# [ ] print the first half of the long_word 
long_word = "Consequences" 
print(long_word[:6])
# [ ] print a message that there is "No Parking" on index 0 or index 4 streets
print("No parking on",long_word[0],"or",long_word[4],"streets.")

#Task 3
#(skipped)

#Task 4
# [ ] print the 1st and every 3rd letter of long_word 
long_word = "Acknowledgement"
print(long_word[::3])
# [ ] print every other character of long_word starting at the 3rd character 
long_word = "Acknowledgement" 
print(long_word[2::2])

#Task 5
# [ ] reverse long_word 
long_word = "stressed" 
print(long_word[::-1])
# [ ] print the first 5 letters of long_word in reverse 
long_word = "characteristics"
print(long_word[4::-1])

#Task 6
long_word = "timeline"
# [ ] print the first 4 letters of long_word
print(long_word[:4])
# [ ] print the first 4 letters of long_word in reverse
print(long_word[3::-1])
# [ ] print the last 4 letters of long_word in reverse
print(long_word[:-5:-1])
# [ ] print the letters spanning indexes 3 to 6 of long_word in Reverse
print(long_word[6:2:-1])