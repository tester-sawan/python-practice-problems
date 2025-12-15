# copy() function is used to copy a dictionary to another dictionary
employee1 = {"Name":"Sawan Kumar","Designation":"QAE","Department":"Quality Engineering","Employee_ID":4082,"Branch":"Noida","Country":"India"}
employee2 = employee1.copy()
employee2.update({"Name":"Harsh Gautam","Employee_ID":4081})
print(employee2)
