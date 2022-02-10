#Will C. & Luke H.
#Python 1
#Unit 1 mod 2 project
# [ ] create, call and test fishstore() function
def fishstore(fish, quantity):
    sentence = "Fish Type: " + fish + " Quantity: " + quantity
    return sentence
in_stock = "salmon, trout, grouper, bass, catfish, flounder"
fish_entry = input("Enter a fish name: ")
quantity = input("How many would you like? ")
fish_stock = (fish_entry.lower() in (in_stock))
stock = fish_stock
if stock==True:
    str_stock = "This fish is in stock"
else:
    str_stock = "This fish is not in stock"
print(fishstore(fish_entry,quantity), str_stock)