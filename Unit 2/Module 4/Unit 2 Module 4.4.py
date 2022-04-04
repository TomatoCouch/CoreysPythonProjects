#Will C.
#Python 1
#Unit 2, Mod 4.4

#Task 1
# [ ] open planets.txt in write mode
inner_planets=open('planets.txt','w')
# [ ] write Mercury, Venus, Earth, Mars on separate lines
inner_planets.write('Mercury\nVenus\nEarth\nMars')
# [ ] close the file and re-open in read mode
inner_planets.close()
inner_planets=open('planets.txt','r')
# [ ] use .read() to read the entire file contents
planets=inner_planets.read()
# [ ] print the entire file contents and close the file
print(planets)
inner_planets.close()

#Task 2
# [ ] open outer_planets.txt in write mode 'w+' 
outer_planets=open('outer_planets.txt','w+')
# [ ] write four outer planets in earth's solar system (Jupiter, Saturn, Uranus, Neptune) on separate
outer_planets.write('Jupiter\nSaturn\nUranus\nNeptune')
# [ ] use .seek() to move the pointer to the start of the file
outer_planets.seek(0)
# [ ] use .read() to read the entire file contents
outerPlanets=outer_planets.read() 
# [ ] print the entire file contents and close the file 
print(outerPlanets)
outer_planets.close()

#Task 3
# [ ] open a new file days.txt in write plus read mode 'w+'
days=open('days.txt','w+')
# [ ] write week days (Monday - Friday) on separate lines to the file
days.write("Monday\nTuesday\nWednesday\nThursday\nFriday")
# [ ] use .seek() to move the pointer to the start of the file
days.seek(0)
# [ ] use .read() to read the entire file contents
daysText=days.read()
# [ ] print the entire file contents and close the file
print(daysText)
# [ ] use .seek() to move the pointer to the end of the file
days.seek(0,2)
# [ ] write the weekend days (Saturday & Sunday)
days.write("\nSaturday\nSunday")
# [ ] use .seek() to move the pointer to the start of the file
days.seek(0)
# [ ] use .read() to read the entire file contents
daysTextNew=days.read()
# [ ] print the entire file contents and close the file
print(daysTextNew)
days.close()

#Task 4
#Open task4_file.txt in append plus mode ("a+")
#Create a  for item in range(5):  loop, for each loop:
#Write to the file: "append #"+ str(item)+"\n"
#Use seek() to set the pointer to the beginning of the file
#Print the file contents using file .read() method after eiting the loop
# [ ] complete the task 
task4_file = open('task4_file.txt', 'w+') 
task4_file.write("Line1\nLine2\nLine3\n") 
task4_file.close() 
# [ ] code here 
task4FileAppend=open('task4_file.txt','a+')
for item in range(5):
    task4FileAppend.write("append #"+str(item)+'\n')
task4FileAppend.seek(0)
task4Text=task4FileAppend.read()
print(task4Text)

#Task 5
#Open task4_file.txt in append plus mode ("r+")
#Create a  for item in range(1,6):  loop, for each loop:
#Write to the file: "write (r+) #"+ str(item)+"\n"
#Use seek(item*11) to set the pointer to 11x's the loop count 
#Note: First loop is 1 if using range(1,6), seek will be set to 11, 22, 33, 44
#Print the file contents using file .read() method after exiting the loop
# [ ] complete the task 
task5_file = open('task5_file.txt', 'w+') 
task5_file.write("Line\nLine2\nLine3\nLine4\nLine5\nLine6\nLine7\nLine8\nLine9\nLine10\n") 
task5_file.seek(0) 
print(task5_file.read(),"\n") 
task5_file.close() 
# [ ] code here 
taskFiveFileAppend=open('task5_file.txt','a+')

for item in range(1,6):
    taskFiveFileAppend.write("write (r+) #"+str(item)+"\n")
    taskFiveFileAppend.seek(item*11)
taskFiveFileAppendText=taskFiveFileAppend.read()
print(taskFiveFileAppendText)