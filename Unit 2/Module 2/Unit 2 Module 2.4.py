#Will C.
#Python 1
#Unit 2, Mod 2.4

#Task 1
# [ ] print ft_bones list 
# [ ] delete "cuboid" from ft_bones 
# [ ] reprint list 
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
print(ft_bones)
del ft_bones[2]
print(ft_bones)

#Task 2
# [ ] print ft_bones list 
# [ ] delete "cuboid" from ft_bones 
# [ ] delete "navicular" from list 
# [ ] reprint list 
# [ ] check for deletion of "cuboid" and "navicular" 
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
print(ft_bones)
del ft_bones[2]
del ft_bones[2]
print(ft_bones)
print("Cuboid: ",'cuboid' in ft_bones)
print("Navicular:",'navicular' in ft_bones)

#Task 3
# [ ] pop() and print the first and last items from the ft_bones list 
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"] 
# [ ] print the remaining list
ft_bone1=ft_bones.pop
ft_bone2=ft_bones.pop
print(ft_bone1,ft_bone2)
print(ft_bones)

#Task 4
#Create a empty list purchase_amounts
#Populate the list with user input for the price of items
#Continue adding to list with  while  until "done" is entered
#Can use while True: with break
#Print purchase_amounts
#[ ] complete the Register Input task above
purchase_amounts=[]
while True:
    price=input("How much did this item cost? ")
    if price.isalpha()==True:
        if price.lower()=='done':
            break
        else:
            pass
    else:
        purchase_amounts.append(price)
print(purchase_amounts)
#Create a subtotal variable = 0
#Create a while loop that runs while purchase_amount (is not empty)
#Inside the loop:
#pop() the last list value cast as a float type
#Add the float value to a subtotal variable
#After exiting the loop print subtotal
#Be sure to populate purchase_amounts by running Part 1 above.
# [ ] complete the Register Total task above
subtotal=0
while purchase_amounts:
    subtotal=subtotal+float(purchase_amounts.pop())
print(subtotal)

#Task 5
# [ ] remove one "Poodle" from the list: dogs, or print "no Poodle found" 
# [ ] print list before and after 
dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]
print(dogs)
while dogs.count('Poodle')>1:
    dogs.remove("Poodle")
    print(dogs)
