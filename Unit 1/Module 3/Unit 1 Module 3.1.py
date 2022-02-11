#Will C.
#Python 1
#Unit 1, mod 3.1
#Task 1

sunny_today = True 
# [ ] test if it is sunny_today and give proper responses using if and else 
if sunny_today==True:
    print("Lovely weather we're having, eh?")
else:
    print("I hate living in Britain.")
sunny_today = False
# [ ] use code you created above and test sunny_today = False 
if sunny_today==True:
    print("Lovely weather we're having, eh?")
else:
    print("I hate living in Britain.")

#Task 2
test_string_1 = "welcome" 
test_string_2 = "I have $3" 
# [ ] use if, else to test for islower() for the 2 strings
if test_string_1.lower()==True:
    print("This string is lower.")
else:
    print("This string is not lower.")

if test_string_2.lower()==True:
    print("This string is lower.")
else:
    print("This string is not lower.")
 
test_string_3 = "With a function it's efficient to repeat code" 
# [ ] create a function w_start_test() use if & else to test with startswith('w') 
def w_start_test(value):
    if value.startswith('w')==True:
        print('"' + value + '"', "starts with w.")
    else:
        print('"' + value + '"',"does not start with w.")
    
# [ ] Test the 3 string variables provided by calling w_start_test() 
print(w_start_test(test_string_1))
print(w_start_test(test_string_2))
print(w_start_test(test_string_3))