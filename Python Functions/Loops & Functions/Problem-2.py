# Write a function to count vowels in a string.
def count_vowel(input):
    input = input.lower()
    vowel = ["a","i","e","o","u"]
    count  = 0
    for char in input:
        for match in vowel:
            if char == match:
                count = count + 1
    return count
print(f"Available vowel in the given input :{count_vowel(input("Enter any string to check vowel count: "))}")