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