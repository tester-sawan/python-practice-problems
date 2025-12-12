"""
Q13. A temperature is stored as:
temp = "38.6C"
Extract the number only and convert it to float.
"""
temp = "38.6C"
temp = float(temp.strip("C"))
print("The type of the variable is:",type(temp))
# _temp,_type = temp.split("C")
# print(_temp)
