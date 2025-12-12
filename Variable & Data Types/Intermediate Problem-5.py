"""
Q10. Write a program to check the type of user input:
Ask user for input
Detect whether input is integer, float, or string
"""

input_num=input("Enter any value: ")
if input_num=="": # Refer empty input or space
    print("Missing input.")
else:
    try:
        input_num=int(input_num)
        print(type(input_num))
    except ValueError:
        try:
            input_num=float(input_num)
            print(type(input_num))
        except ValueError:
             print(type(input_num))