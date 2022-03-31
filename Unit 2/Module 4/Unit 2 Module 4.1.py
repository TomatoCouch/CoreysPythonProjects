#Will C.
#Python 1
#Unit 2, Mod 4.1
#This whole thing is broken, I'm taking a look at it eventually

#Task 1
cities_file=open('cities.txt','r')
print(cities_file)

#Task 2
# [ ] after import and open of cities.txt in task 1 
# [ ] read cities_file as cities 
cities=cities_file.read()
# [ ] display the string: cities 
cities
# [ ] print the string: cities 
print(cities)

#Task 3
# [ ] digits of pi 
# 2. open as digits_of_pi_text
digits_of_pi_text=open('digits_of_pi.txt')
# 3. read() 4 char of digits_of_pi_text to pi_digits variable
pi_digits=digits_of_pi_text.read(4)
# 4. print pi_digits
print(pi_digits)
# 5. add to pi_digits string with string addition
#   a. add next 4 characters from digits_of_pi obtained from read()   
#   b. run the cell multiple times to get more digits of *pi*
nextFourPi=digits_of_pi_text.read(4)
print(pi_digits+nextFourPi)

#Task 4
#1. Ensure the code was created and run in Task 1 to import cities.txt
#2. Create and run code to re-open cities.txt as cities_file
#3.  read()  cities_file into a variable called cities
#4. Iterate through the characters in cities a. Test if .isupper(), if True append the character to a string variable: initials c. Else if (elif) character is "\n", if True append the
#"\n" to initials
#5. Print initials
cities_file=open('cities.txt','r')
cities=cities_file.read()
counter=1
initial=""
for character in cities:
    if character[counter].isupper()==True:
        initial+=character