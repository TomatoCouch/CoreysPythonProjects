import os
cwd=os.getcwd
os.chdir("C:/Users/Chloe/Music/Gaming Music Return")
print("directory: "+os.getcwd())
#now:
for item in os.listdir():
    print('C:/Users/Chloe/Music/Gaming Music Return/'+item[0:item.find("-")]+".mp3")
    os.rename(r'C:/Users/Chloe/Music/Gaming Music Return/'+item,r'C:/Users/Chloe/Music/Gaming Music Return/'+item[item.find("- ")+2:])