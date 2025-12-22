# Write a function to return all even numbers from a list.
list = [1,2,3,4,5,6,7,8,9,10]
def filter_even(data):
    even_list=[]
    for num in data:
        if num % 2==0:
            even_list.append(num)
    return even_list
print(filter_even(list))


