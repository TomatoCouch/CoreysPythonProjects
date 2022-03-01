#Will C.
#Python 1
#Unit 1, Mod 4.3

#Task 1
# [ ] create Get Name program
while True:
    name=input("What is your name?")
    if name.isalpha()==True:
        print("Hello,",name+"!")
        break
    else:
        pass

#Task 2
#With Luke and Colin
# [ ] Create the Shirt Count program, run tests
small=0
medium=0
large=0
small_cost=6
medium_cost=7
large_cost=8
while True:
    print("Enter a shirt size:")
    size=input("s, m, l, or exit ").lower()
    if size=="s":
        small+=1
    elif size=="m":
        medium+=1
    elif size=="l":
        large+=1
    elif size=="exit":
        shirt_total=small+medium+large
        print("Size\tAmount\tPrice per unit\tTotal price\nSmall\t"+str(small)+"\t"+str(small_cost)+"\t\t"+str(small*small_cost)+"\nMedium\t"+str(medium)+"\t"+str(medium_cost)+"\t\t"+str(medium*medium_cost)+"\nLarge\t"+str(large)+"\t"+str(large_cost)+"\t\t"+str(large*large_cost))
        print("Total:\t"+str(shirt_total)+"\t\t\t"+str((small*small_cost)+(medium*medium_cost)+(large*large_cost)))
        break
    else:
        print("Unknown input.")