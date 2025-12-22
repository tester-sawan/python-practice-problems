# Write a function to return the sum of digits of a number.
def sum_of_digit(num):
    result = 0
    for i in range(0,len(num)):
        result = result + int(num[i])
    return result
try:
    print(sum_of_digit(input("Enter the number to find out their sum: ").strip()))
except ValueError:
    print("Invalid literal, Use only numbers.")
