#Loops through a dictionaries.
employee1 = {"Name":"Sawan Kumar","Designation":"QAE","Department":"Quality Engineering","Employee_ID":4082,"Branch":"Noida","Country":"India"}
# Use for loop to iterate the dict - employee1
for x in employee1:
    print(x) #This will return the keys values form the dictionary.
# Use for loop with keys() methods to get all the keys.
for keys in employee1.keys():
    print(keys,end=" ")
print()
# Use for loop with the values() methods to get all the values.
for values in employee1.values():
    print(values,end=" ")
print()
# Use for loop with the items() to get the keys & values from a dictionaries
for keys,values in employee1.items():
    print(f"{keys}:{values}")