#Will C.
#Python 1
#Unit 1, mod 2.3

#Task 1
# [ ] fix the sequence of the code to remove the NameError 
#have_hat = hat_available('green')   
#print('hat available is', have_hat) 
#def hat_available(color): 
#    hat_colors = 'black, red, blue, green, white, grey, brown, pink' 
#    return(color.lower() in hat_colors) 
def hat_available(color): 
    hat_colors = 'black, red, blue, green, white, grey, brown, pink' 
    return(color.lower()) in (hat_colors) 
have_hat = hat_available('green')
print('hat available is', hat_available)

#Task 2
# [ ] create function bird_available 
def bird_available(bird):
    bird_types = 'crow robin parrot eagle sandpiper hawk pigeon'
    return (bird.lower())in(bird_types)
# [ ] user input
bird_choice = input("Enter a bird: ")
# [ ] call bird_available
ba = bird_available(bird_choice)
# [ ] print availability status
print("Bird available?", ba)

#Task 3
# define function how_many 
def how_many(): 
    requested = input("enter how many you want: ") 
    return requested 
# get the number_needed 
number_needed = how_many() 
print(number_needed, "will be ordered") 