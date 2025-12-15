employee1 = {"Name":"Sawan Kumar","Designation":"QAE","Department":"Quality Engineering","Employee_ID":4082,"Branch":"Noida","Country":"India"}
# Get the value for the given key:
# Method-1:
print(employee1["Name"])#Return the value for the specified key.
# Method-2
print(employee1.get("Name"))
# Modify the current dictionary
employee1["Name"] = "Harsh Gautam"
print(employee1)
employee1.update({"Name":"Sawan Kumar","Designation":"QA-2"}) #If not found will add as a new key-value pair
print(employee1)
# Add a new key-value pair
# update()
# Get all keys from a dictionary
print(employee1.keys())
# Get all values from a dictionary
print(employee1.values())
# Get all items
print(employee1.items())
# remove a single key-value from a dictionary
print(employee1.pop("Designation")) # retuns the value of the deleted keys.
print(employee1)
print(employee1.popitem()) #Removes the last item from a dict and returns key-value
print(employee1.clear()) #clear all values.
print(employee1)