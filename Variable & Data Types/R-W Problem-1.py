"""
Q11. A variable contains a CSV string:
data = "John,30,Developer,55000"
Split and store:
name
age
role
salary (as integer)
"""
name,age,role,salary="John,30,Developer,55000".split(",")
salary = int(salary)
print("Name:",name)
print("Age:",age)
print("Role:",role)
print("Salary:",salary)