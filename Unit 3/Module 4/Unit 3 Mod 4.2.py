#Will C.
#Python 1
#Unit 3, Mod 4.2

#Task 1
# [ ] Fix the program below so it displays the area of a square with a side = 2 
# Compute the area of a square 
def square_area (side):
    global area
    # area is a local variable in square_area 
    area = side ** 2 
    return area 
# Global scope 
square_area(2) 
# area is not within scope anymore and cannot be 
# accessed from this global scope 
print(area)
# [ ] Fix the program below so it displays the area of a square with side = 2 
# and the volume of a cube with side = 2 
# Compute the area of a square 
def square_area (side): 
    # area is a local variable in square_area 
    area = side ** 2 
    return area 
# Compute the volume of a cube 
def cube_volume (side): 
    # cube volume = area of base X side 
    volume = area * side # area is not defined within this scope 
    return volume 
# Global scope 
s = 2 
square_area(s) 
# area was deleted when the local scope of square_area was destroyed 
cube_volume(s) 
# [ ] The program below converts US Dollars to Euros, British Pounds, and Japanese Yen 
# Complete the functions USD2EUR, USD2GBP, USD2JPY so they all return the correct value 
def USD2EUR(amount):
    """ 
    Convert amount from US Dollars to Euros. 
     
    Use 1 USD = 0.831467 EUR 
     
    args: 
        amount: US dollar amount (float) 
         
    returns: 
        value: the equivalent of amount in Euros (float) 
    """ 
    value=amount*.831467
    return value 
def USD2GBP(amount): 
    """ 
    Convert amount from US Dollars to British Pounds. 
     
    Use 1 USD = 0.739472 GBP 
     
    args: 
        amount: US dollar amount (float) 
         
    returns: 
        value: the equivalent of amount in British Pounds (float) 
    """ 
    value=amount*.73942
    return value 
def USD2JPY(amount): 
    """ 
    Convert amount from US Dollars to Japanese Yen. 
     
    Use 1 USD = 112.656 JPY 
     
    args: 
        amount: US dollar amount (float) 
         
    returns: 
        value: the equivalent of amount in Japanese Yen (float) 
    """ 
    value=amount*112.656
    return value 
def main(): 
    amount = float(input("Enter amount in USD: $")) 
     
    # In Euros 
    eur = USD2EUR(amount) 
     
    # In British Pounds 
    gbp = USD2GBP(amount) 
     
    # In Japanese Yen 
    jpy = USD2JPY(amount) 
     
    print("${:.2f} USD = {:.2f} EUR, {:.2f} GBP, {:.2f} JPY".format(amount, eur, gbp, jpy)) 

#Tssk 2
# [ ] The program below converts US Dollars to British Pounds. However, the conversion rate is unknow
# Complete the functions USD2EUR, EUR2GBP, and USD2GBP so they all return the correct value 
# You should use USD2EUR and EUR2GBP in USD2GBP, do not try to find out the conversion rate 
def USD2EUR(amount): 
    """ 
    Convert amount from US Dollars to Euros. 
     
    Use 1 USD = 0.831467 EUR 
     
    args: 
        amount: US dollar amount (float) 
         
    returns: 
        value: the equivalent of amount in Euros (float) 
    """ 
    value=USD2EUR(amount)
    return value 
def EUR2GBP(amount): 
    """ 
    Convert amount from Euros to British Pounds. 
     
    Use 1 EUR = 0.889358 GBP 
     
    args: 
        amount: Euros amount (float) 
         
    returns: 
        value: the equivalent of amount in GBP (float) 
    """ 
    value=USD2EUR(amount)
    value=EUR2GBP(value) 
    return value 
def USD2GBP(amount): 
    """ 
    Convert amount from US Dollars to British Pounds. 
     
    The conversion rate is unknown, you have to use USD2EUR and EUR2GBP 
     
    args: 
        amount: US dollar amount (float) 
         
    returns: 
        value: the equivalent of amount in British Pounds (float) 
    """ 
    value=USD2GBP(amount)
    return value 
def main(): 
    amount = float(input("Enter amount in USD: $")) 
     
    # In British Pounds 
    gbp = USD2GBP(amount) 
     
    print("${:.2f} USD = {:.2f} GBP".format(amount, gbp)) 
     
if __name__ == '__main__': 
    main() 