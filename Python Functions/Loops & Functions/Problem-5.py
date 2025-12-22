# Write a function to check if a string is a palindrome.
def check_palindrome(value):
    _reverse = value[::-1]
    if value == _reverse:
        return "Palindrome"
    else:
        return "not a palindrome"
print(check_palindrome("harsh"))