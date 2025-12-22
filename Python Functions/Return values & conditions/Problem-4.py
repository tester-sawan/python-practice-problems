# Write a function to return the factorial of a number.
def fact(number):
    result = 1
    for num in range(1,number+1):
        result = result*num
    return result


print("factorial: ",fact(3))
print("factorial: ",fact(4))