# Write a function to check whether a number is even or odd.
def check_even_odd(num):
    if num%2 ==0:
        return "Even"
    else:
        return "Odd"
result = check_even_odd(1)
print("Result:",result)