#Will C.
#Python 1
#Unit 2, Mod 1.1

#Task 1
# [ ] assign a string 5 or more letters long to the variable: street_name
street_name="Kildaire Farm"
# [ ] print the 1st, 3rd and 5th characters 
print(street_name[1],street_name[3],street_name[5])
# [ ] Create an input variable: team_name - ask that second letter = "i", "o", or "u" 
team_name=input("enter a team name with second letter\"i,o , or u\": ")
# [ ] Test if team_name 2nd character = "i", "o", or "u" and print a message 
# note: use if, elif and else
if team_name[1].lower()=="i":
    print("Good Team name,",team_name,"has second letter\"i\"")
elif team_name[1].lower()=="u":
    print("Good Team name,",team_name,"has second letter\"u\"")
elif team_name[1].lower()=="o":
    print("Good Team name,",team_name,"has second letter\"o\"")
else:
    print("Team name error,", team_name,"has second letter",""+team_name[1]+"")

#Task 2
# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the last 3 characters of street_name 
print(street_name[-1],street_name[-2],street_name[-3])
# [ ] create and assign string variable: first_name
first_name="Will"
# [ ] print the first and last letters of name 
print(first_name[0],first_name[-1])
# [ ] Review, Run, Fix the error using string index 
#shoe = "tennis" 
# print the last letter 
#print(shoe(-1))
shoe="tennis"
print(shoe[-1])