#Will C.
#Python 1
#Unit 3, Mod 1.4

#import
import os

#Task 1
# [ ] Write a program to: 
# 1) Prompt the user for a directory name 
dir_name=input("Enter a directory name: ")
# 2) Create the directory 
print("Making",dir_name)
os.mkdir(dir_name)
# 3) Verify the directory was created by listing the content of the current working directory
print(os.listdir())
# 4) Remove the created directory
os.rmdir(dir_name)
# 5) Verify the directory was removed by listing the content of the current working directory 
print(os.listdir())

#Task 2
# [ ] Write a program that prompts the user for a file or directory name
name=input("Enter a file/directory name: ")
# then prints a message verifying if it exists in the current working directory
if os.path.isdir(name)==True:
    print("Real directory!")
else:
    print("Fake directory.")
# [ ] Write a program to print the absolute path of all directories in "parent_dir"
# HINTS: 
# 1) Verify you are inside "parent_dir" using os.getcwd() 
# 2) Use os.listdir() to get a list of files and directories in "parent_dir" 
# 3) Iterate over the elements of the list and print the absolute paths of all the directories
if os.getcwd=="parent_dir":
    dadDir=os.listdir()
    for dir in dadDir:
        print(os.path.abspath(dir))
    else:
        print("Not in parent_dir")