#Will C.
#Python 1
#Unit 2, Mod 4.2
#Still broken

#Task 1
# [ ] import cities
# [ ] open cities.txt as cities_file and read the file as a list: cities_lines 
cities_file=open('cities.txt','r')
# [ ] use list iteration to print each city in cities_lines list 
cities_lines=cities_file.readlines()
print(cities_lines)

#Task 2
# [ ] re-open file and read file as a list of strings
cities_file=open('cities.txt','r')
# [ ] open cities.txt as cities_file and read the file as a list: cities_lines
cities_lines=cities_file.readlines()
# [ ] remove the last character, "\n", of each cities_lines list item
counter=0
for line in cities_lines:
    cities_lines[counter]=line[:-1]
    counter+=1
print(cities_lines)

#Task 3
# [ ] open cities.txt as cities_file
cities_file=open('cities.txt','r')
# [ ] read the lines as cities_lines
cities_lines=cities_file.readlines()
# [ ] print the cities that start with the letter "D" or greater 
for city in cities_lines:
    if city[0]>='D':
        print(city)
# [ ] test that file is closed 
print(cities_file)
# [ ] close cities_file
cities_file.close()

#Task 4
# [ ] open poem2.txt as poem2_text in read mode
poem2_text=open('poem2.txt','r')
# [ ] create a list of strings, called poem2_lines, from each line of poem2_text
poem2_lines=poem2_text.readlines()
# [ ] remove the newline character for each list item in poem2_lines
counter=0
for line in poem2_lines:
    poem2_lines[counter]=line[:-1]
    counter+=1
print(poem2_lines)
# [ ] print the poem2 lines in reverse order
for line in poem2_lines[::-1]:
    print(line)