#Will C.
#Python 1
#Unit 2, Mod 4.3

#Task 1
# [ ] open rainbow.txt as rainbow_text 
rainbow_text=open('rainbow.txt','r')
# [ ] read the first 3 lines into variables: color1, color2, color3 
color1=rainbow_text.readline()
color2=rainbow_text.readline()
color3=rainbow_text.readline()
# [ ] close rainbow.txt 
rainbow_text.close()
# [ ] print the first 3 colors
print(color1+color2+color3)

#Task 2
# [ ] open rainbow.txt as rainbow_text as read-only 
rainbow_text=open('rainbow.txt','r')
# [ ] read the color from lines of rainbow_text in a while loop
# [ ] print each color capitalized as the loop runs
color=rainbow_text.readline()
while color:
    print(color[:-1].upper())
    color=rainbow_text.readline()
# [ ] close rainbow_text
rainbow_text.close()

#Task 3
# [ ] open rainbow.txt as rainbow_text as read-only
rainbow_text=open('rainbow.txt','r')
# [ ] read a color from each line of rainbow_text in a while loop   
# use .strip to remove the whitespace '\n' character  
# print each color upper case
color=rainbow_text.readline().strip()
while color:
    print(color.upper())
    color=rainbow_text.readline().strip()
rainbow_text.close()

#Task 4
# [ ] run to read the file into memory 
cities_messy = open('cities_messy.txt', 'r') 
# [ ] edit the code to remove leading or trailing colon, newline and space characters 
line = cities_messy.readline().strip(':\n ')
while line: 
    print(line) 
    line = cities_messy.readline().strip(':\n ')

#Task 5
# [ ] open poem2_messy.txt as poem2_messy in read mode
poem2_messy=open('poem2_messy.txt','r')
# [ ] edit while loop to strip the leading and trailing parenthesis, and newlines 
# [ ] print the poem  
line = poem2_messy.readline().strip('()\n ')
while line: 
    print(line) 
    line = poem2_messy.readline().strip('()\n ')