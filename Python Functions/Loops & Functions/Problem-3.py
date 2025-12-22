# Write a function to reverse a string without using slicing.
def reverse(value):
    _length = len(value)
    _reverse = []
    for i in range(len(value)-1,-1,-1):
        _reverse.append(value[i])
    return "".join(_reverse)
print(reverse("sawan"))