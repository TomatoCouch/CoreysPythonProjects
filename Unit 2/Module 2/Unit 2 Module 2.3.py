#Will C.
#Python 1
#Unit 2, Mod 2.3

#Task 1
#Create a list,  three_num , containing 3 single digit integers
#Print three_num
#Check if index 0 value is < 5
#if < 5 , replace index 0 with a string: "small"
#else, replace index 0 with a string: "large"
#Print three_num
# [ ] complete "replace items in a list" task
three_num=[1,2,3]
if three_num[0]<5:
    three_num[0]="small"
else:
    three_num[0]="large"
print(three_num)
#Create a function, str_replace, that takes 2 arguments: int_list and index
#int_list is a list of single digit integers
#Index is the index that will be checked - such as with int_list[index]
#Function replicates purpose of task "replace items in a list" above and replaces an integer with a string "small" or "large"
#Return str_list
#Test the function!
# [ ]  create challenge function
int_list=[1,5,7,5,34,8,6,4,8,4]
def str_replace(int_list,index):
    if int_list[index]<5:
        int_list[index]="small"
    else:
        int_list[index]="large"
    return int_list
print(str_replace(int_list,3))

#Task 2
#Create a list,  three_words , containing 3 different capitalized word strings
#Print three_words
#Modify the first item in three_words to uppercase
#Modify the third item to swapcase
#Print three_words
# [ ] complete coding task described above
three_words=["One","Two","Three"]
three_words[0]=three_words[0].upper()
three_words[1]=three_words[1].swapcase()
print(three_words)

#Task 3
# [ ] insert a name from user input into the party_list in the second position (index 1) 
party_list = ["Joana", "Alton", "Tobias"] 
party_list[1]=input("Enter a name:")
# [ ] print the updated list
print("party_list=",party_list)

#Task 4
# [ ] Fix the Error 
#tree_list = "oak" 
#print("tree_list before =", tree_list) 
#tree_list.insert(1,"pine") 
#print("tree_list after  =", tree_list)
#set tree_list as a string
# [ ] Fix the Error 
tree_list=["oak"]
print("tree_list before =",tree_list) 
tree_list.insert(1,"pine") 
print("tree_list after  =",tree_list)