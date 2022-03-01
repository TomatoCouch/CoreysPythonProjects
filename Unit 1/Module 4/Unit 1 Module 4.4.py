#Will C.
#Python 1
#Unit 1, Mod 4.4

#Task 1
# [ ] Create the Animal Names program, run tests
num_animals=0
while True:
    animal=input("Input an animal. To quit, input \"Quit\" ").lower()
    if animal.isalpha()==True and animal!="quit":
        num_animals+=1
        if num_animals>=4:
            print("Animal limit reached.")
            break
    elif animal.isalpha()==True and animal=="quit":
        print("Quitting...") 
        break
    else:
        print("Unexpected input.")

#Task 2
# [ ] Create the program, run tests
long_num=""
while True:
    int_num=input("Enter a number: ")
    if int_num.isdigit()==True:
        long_num=long_num+int_num
    else:
        print("Not a number, printing and quitting:\n"+long_num)
        break

#Task 3
# [ ] review the code, run, fix the Logic error 
#count = 1 
# loop 5 times 
#while count > 6: 
#    print(count, "x", count, "=", count*count) 
#    count +=1
# [ ] review the code, run, fix the Logic error 
count = 1 
# loop 5 times 
while count < 6: 
    print(count, "x", count, "=", count*count) 
    count +=1