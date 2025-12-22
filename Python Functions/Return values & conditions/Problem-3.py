# Write a function is_prime(n) that returns True if prime else False.
def is_prime(n):
    if n<=1:
        return "Not a prime number."
    for i in range(2,(n+1)):
        if n%i==0:
            return "not prime"
        return "prime"

result = is_prime(10)
print(result)