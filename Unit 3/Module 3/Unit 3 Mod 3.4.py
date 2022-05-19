#Will C.
#Python 1
#Unit 3, Mod 3.4

#Task 1
# [ ] The `data` list contains information about a company's employees.
# Use the `data` list and an appropriate loop to create a dictionary of employees.
# Use IDs (as keys) and names (as values).
# Ignore the email addresses for now.
# The created dictionary should look like:
# {57394: 'Suresh Datta', 48539: 'Colette Browning', 58302: 'Skye Homsi', 48502: 'Hiroto Yamaguchi', 48291: 'Tobias Ledford', 48293: 'Jin Xu', 23945: 'Joana Dias', 85823: 'Alton Derosa'}
data = [["Suresh Datta", 57394, "suresh@example.com"], ["Colette Browning", 48539, "colette@example.com"], ["Skye Homsi", 58302, "skye@example.com"], ["Hiroto Yamaguchi", 48502, "hiroto@example.com"], ["Tobias Ledford", 48291, "tobias@example.com", "Tamara Babic", 58201, "tamara@example.com"], ["Jin Xu", 48293, "jin@example.com"], ["Joana Dias", 23945, "joana@example.com"], ["Alton Derosa", 85823, "alton@example.com"]]
D={}
for record in data:
    D[record[1]]=record[0]
print(D)
# [ ] Use the `records` dictionary in a program that asks the user for an ID and prints the name of the associated employee.
records = {57394: 'Suresh Datta', 48539: 'Colette Browning', 58302: 'Skye Homsi', 48502: 'Hiroto Yamaguchi', 48291: 'Tobias Ledford', 48293: 'Jin Xu', 23945: 'Joana Dias', 85823: 'Alton Derosa'}
try: 
  id=int(input("Enter employee ID: "))
  name=records[id]
  print("Name:",name)
# Display an appropriate message if the ID is not found in the dictionary.
except KeyError:
  print("Employee ID not found.")
except ValueError:
  print("Numbers only.")
# [ ] Use the `records` dictionary in a program to ask the user for an ID then delete the employee record associated with the ID
records = {57394: 'Suresh Datta', 48539: 'Colette Browning', 58302: 'Skye Homsi', 48502: 'Hiroto Yamaguchi', 48291: 'Tobias Ledford', 48293: 'Jin Xu', 23945: 'Joana Dias', 85823: 'Alton Derosa'}
try: 
  id=int(input("Enter employee ID: "))
  name=records[id]
  delEmp=records.pop(id)
  print("Deleting:",delEmp)
# The program should display an appropriate message if the ID is not found in the dictionary.
except KeyError:
  print("Employee ID not found.")
except ValueError:
  print("Numbers only.")
#Task 2
# [ ] The `data` list contains information about a company's employees
# Use the `data` list and an appropriate loop to create a dictionary of
# IDs (as keys): [name, email] (as values)
# The resulting dictionary should look like:
# {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
data = [["Suresh Datta", 57394, "suresh@example.com"], ["Colette Browning", 48539, "colette@example.com"], ["Skye Homsi", 58302, "skye@example.com"], ["Hiroto Yamaguchi", 48502, "hiroto@example.com"], ["Tobias Ledford", 48291, "tobias@example.com", "Tamara Babic", 58201, "tamara@example.com"], ["Jin Xu", 48293, "jin@example.com"], ["Joana Dias", 23945, "joana@example.com"], ["Alton Derosa", 85823, "alton@example.com"]]

# [ ] Write a program to display the content of the `records` dictionary as shown here
# Note the IDs are sorted in an ascending order
print("{0:^20s} | {1:10s} | {2:^20s}")
'''
      Name         |     ID     |        Email
______________________________________________________
   Joana Dias      |   23945    |    joana@example.com
 Tobias Ledford    |   48291    |   tobias@example.com
     Jin Xu        |   48293    |      jin@example.com
Hiroto Yamaguchi   |   48502    |   hiroto@example.com
Colette Browning   |   48539    |  colette@example.com
  Suresh Datta     |   57394    |   suresh@example.com
   Skye Homsi      |   58302    |     skye@example.com
  Alton Derosa     |   85823    |    alton@example.com
'''
records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
# [ ] The company's domain has changed from (example.com) to (example.org)
# Write a program to modify the email addresses in the `records` dictionary to reflect this change
for id in records:
  oldEmail=records[id][1]
  username=oldEmail.split('@')[0]
  newEmail=username+"example.org"
records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
# [ ] You want to send a mass email to all company employees, so you need a list of all the email addresses in `records`
# Write a program to extract the email addresses from the `records` dictionary and store them in a list
# The output list should look like:
# ['suresh@example.com', 'colette@example.com', 'skye@example.com', 'hiroto@example.com', 'tobias@example.com', 'jin@example.com', 'joana@example.com', 'alton@example.com']
# Hint: use the `.values()` method
records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
emailList=list(records.values())
print(emailList)
# [ ] Write a program to find out the number of employees stored in `records`.
records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}

#Task 3
# Write a program that can ONLY update the price of an existing grocery  
# in the `groceries` dictionary. 
# The item and updated price should be entered by the user. 
# If the user enters a new item, the program should not create  
# a new dictionary item. It should instead display an error message.
item=input("Enter an item on your grocery list.")
groceries = {'Bread':2.26, 'Milk':3.62, 'Chocolate':1.59}
if (item in groceries):
  price=float(input("Enter the updated price: "))
  groceries[item]=price
  print("Updated grocery list:\n",groceries)
else:
  print(item,"was not found on your grocery list.")