# age = input("what is your age? ")
# data_type = type(age)
# print(data_type)
# #all input starts as string
# age = int(age)
# data_type = type(age)
# print(data_type)

# print("age in dog years is ", (age * 7))

grocery_list = ['apples', 'oranges', 'bananas', 'apples']
grocery_list = set(grocery_list)
#apples only shows up once becasue this is a set
print(grocery_list)
print(type(grocery_list))

grocery_list = tuple(grocery_list)
print(grocery_list)
print(type(grocery_list))

grocery_list = list(grocery_list)
print(grocery_list)
print(type(grocery_list))