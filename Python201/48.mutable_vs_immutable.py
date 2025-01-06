string = "fox jumped over cow"
string = "overwritten"
#this isnt mutable - its being replaced
print(string.upper())
print(string)

names = ["john","joe","smith"]
#the list itself is mutable
names.append("potato")
#new list is saved - unlike uppercase string
print(names)

