#Will C.
#Python 1
#Unit 2, Mod 3.3

#Task 1
# [ ] extend the list common_birds with list birds_seen which you must create 
common_birds = ["chicken", "blue jay", "crow", "pigeon"] 
birdsSeen=['cardinal','robin','owl','wren']
print(common_birds+birdsSeen)
# [ ] Create 2 lists zero_nine and ten_onehundred that contain 1-9, and 10 - 100 by 10's. 
# [ ] use list addition to concatenate the lists into all_num and print
zeroNine=[1,2,3,4,5,6,7,8,9]
tenOneHundred=[10,20,30,40,50,60,70,80,90,100]
allNum=zeroNine+tenOneHundred
print(allNum)

#Task 2
# [ ] create and  print a list of multiples of 5 from 5 to 100 
multiplesOf5=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
print(multiplesOf5)
# { ] reverse the list and print 
print(multiplesOf5.reverse())
# [ ] Create two lists: fours & more_fours containing multiples of four from 4 to 44 
fours=[4,8,16,20,24,28,32,36,40,44]
moreFours=[4,8,16,20,24,28,32,36,40,44]
print(type(moreFours))
# [ ] combine and print so that the output is mirrored [44, 40,...8, 4, 4, 8, ...40, 44]
moreFours.reverse()
print(fours+moreFours)

#Task 3
# [ ] print cites from visited_cities list in alphbetical order using .sort() 
# [ ] only print cities that names start "Q" or earlier 
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
visited_cities.sort()
for city in visited_cities:
    if city <='Q':
        print(city)
    else:
        pass
# [ ] make a sorted copy (sorted_cities) of visited_cities list
sorted_cities=sorted(visited_cities)
for city in sorted_cities:
    if len(city)<=5:
        sorted_cities.remove(city)
    else:
        pass

# [ ] remove city names 5 characters or less from sorted_cities 
for city in sorted_cities:
    if len(city)<=5:
        sorted_cities.remove(city)
    else:
        pass
# [ ] print visitied cites and sorted cities
print(sorted_cities)
print(visited_cities)

#Task 4
#Create a program that
#takes user to build a list: add_animals
#merges add_anmials with exisiting list: anmimals
#provides a sorted list to view in alpa or reverse alpha order
#step 1 get user input to build add_animals list
# [ ] build a list (add_animals) using a while loop, stop adding when an empty string is entered 
#add_animals = [] 
#step 2 Merge the lists: add_animals into animals
# [ ] extend the lists into animals, then sort  
#animals = ["Chimpanzee", "Panther", "Wolf", "Armadillo"] 
#step 3 Allow animals list to be viewed alpha or reverse alpha order
# [ ] get input if list should be viewed alpha or reverse alpha and display list 
addAnimals=[]
while True:
    newAnimal=input("Input an animal. To quit, enter 'Quit': ")
    if newAnimal.lower()!="quit":
        addAnimals.append(newAnimal)
    else:
        break
sortedAnimals=sorted(addAnimals)
reversedAnimals=list(reversed(sortedAnimals))
while True:
    alpOrRev=input("To view your list in order from A-Z, enter 'A'. To view your list in order from Z-A, enter 'Z'. To quit, enter 'Quit': ")
    if alpOrRev.lower()=="a":
        print(sortedAnimals)
    elif alpOrRev.lower()=="z":
        print(reversedAnimals)
    elif alpOrRev.lower()=="quit":
        break
    else:
        print("Unexpected input.")
