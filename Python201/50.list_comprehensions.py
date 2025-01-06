#short hand method of for loop
#and putting the data into a list

numbers = []
for num in [1,3,5,7,9]:
    numbers.append(num**2)
print(numbers)
#these are the same thing
numbers = [num**2 for num in [1,3,5,7,9]]
print(numbers)