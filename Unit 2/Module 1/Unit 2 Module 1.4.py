#Will C.
#Python 1
#Unit 2, Mod 1.4

#Task 1
# [ ] use len() to find the midpoint of the string  
# [ ] print the halves on separate lines 
random_tip = "wear a hat when it rains"
mid_pt=int(len(random_tip)/2)
print(random_tip[:mid_pt])
print(random_tip[mid_pt:])

#Task 2
# for letters: "e" and "a" in random_tip 
# [ ] print letter counts  
# [ ] BONUS: print which letter is most frequent 
random_tip = "wear a hat when it rains"
e_in_tip=random_tip.find("e")
a_in_tip=random_tip.find("a")
print("'E' count:",e_in_tip)
print("'A' count:",a_in_tip)
if e_in_tip<a_in_tip:
    print("'A' appears more times than 'E' in that tip.")
elif e_in_tip==a_in_tip:
    print("'E' and 'A' appear an equal amount of times in that tip.")
else:
    print("'E' appears more times than 'E' in that tip.")

#Task 3
# [ ] print long_word from the location of the first and second "t" 
long_word = "juxtaposition"
firstT=long_word.find("t"[:5])
secondT=long_word.find("t"[5:7])
print(secondT)
print(long_word[firstT:])
print(long_word[secondT:])

#Task 4
quote = "they stumble who run fast" 
start = 0 
space_index = quote.find(" ") 
while space_index != -1: 
    # code to print word (index slice start:space_index)
    print(quote[start:space_index])
    start=next_space+1
    next_space=quote.find(" ",start)
print(quote[start:])