print("HVM Operating System (version 0.000001)\n\n\n\n\nNot Copyright Project HVM 2023")
mode="itemSelect"
itemsList={1:"chease"}
if mode=="itemSelect":
    print("Current mode: Item Select\nTo switch to Item Insert, enter \"switch\"")
    id=str(input("Enter item ID: "))
    if int(id) in itemsList.keys():
        print("Item:\n"+itemsList.get(id),"\nVend? [Y/N]")
        vend=input()
        if vend.lower()=="y":
            print("Vending...")
        elif vend.lower()=="n":
            print("Returning to selection...")