# Write a function that returns the second largest number in a list.
num_list = [1,2,5,3,10]
def second_largest(num_list):
    unique_name = list(set(num_list))
    unique_name.sort(reverse=True)
    return unique_name[1]
print(second_largest(num_list))
    