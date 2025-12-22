# Write a function to check whether a number is positive, negative, or zero.
def number_type(number):
    if number<0:
        return "negative"
    elif number>0:
        return "positive"
    elif number == 0:
        return "zero"
    else:
        return "Some unkown error reported."
try:
    num = float(input("Enter any number: "))
    result = number_type(num)
    print(result)
except TypeError:
    print("Correct the input type. Accept only numbers.")
except ValueError:
    print("Correct the input type. Accept only numbers.")
