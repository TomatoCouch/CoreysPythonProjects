#Will C.
#Python 1
#Unit 2, Mod 3.1

#Task 1
# [ ] create a list of 4 to 6 strings: birds 
# print each bird in the list 
counter=0
birds=["sandpiper","tit","bluejay","cardinal"]
while counter!=len(birds):
    print(birds[counter])
    counter+=1
# [ ]  create a list of 7 integers: player_points 
player_points=[7,345,6923865,1835601395,2856982436923865,238693768719649264,9265387461987451289654164512984]
# [ ] print double the points for each point value
counter=0
while counter!=len(player_points):
    print(player_points[counter]*2)
    counter+=1

# [ ] create long_string by concatenating the items in the "birds" list previously created 
# print long_string - make sure to put a space betweeen the bird names
counter=0
long_string=""
while counter!=len(birds):
    long_string=birds[counter]+" "+long_string
    counter+=1
print(long_string)

#Task 2
# [ ] Using cities from the example above iterate throught the list using "for"/"in" 
# [ ] Print only cities starting with "m" 
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
counter=0
while counter!=len(cities):
    if (cities[counter].lower()).startswith('m'):
        print(cities[counter])
        counter+=1
    else:
        counter+=1
# [ ] Using cities from the example above iterate throught the list using "for"/"in" 
# cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"] 
for city in cities:
    print(city)
# [ ] sort into lists with "A" in the city name and without "A" in the name: a_city & no_a_city
counter=0
while counter!=len(cities):
    if 'a' in cities[counter].lower()==True:
        print(cities[counter])
        counter+=1
    else:
        counter+=1

#Task 3
#Create list, paint_colors, with 5+ colors
paint_colors=["green","blue","yellow","purple","red"]
#Get user input of string:color_request
color_request=input("Pick a color: ")
#Iterate through each color in paint_colors to check for a match with color_request
counter=0
in_stock=[]
while counter!=len(paint_colors):
    if color_request.lower()==paint_colors[counter]:
        in_stock.append("Yes")
        counter+=1
    else:
        in_stock.append("No")
        counter+=1
if in_stock.count("Yes")!=0:
    print("Paint is in stock!")
else:
    print("Paint is out of stock.")

#Task 4
#Call the function 2 times with the name of a footbone
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
#print immediate feedback for each answer (correct - incorrect)
#print the total # of foot_bones identified
def foot_bone_quiz(bone):
    if foot_bones.count(bone)!=0:
        print("Correct bone!")
    else:
        print("Incorrect bone.")
bone=input("Guess a foot bone! ").lower()
foot_bone_quiz(bone)
bone=input("Guess a foot bone! ").lower()
foot_bone_quiz(bone)