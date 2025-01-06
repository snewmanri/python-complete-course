# names = ['joe','steve','alex']
# type(names)
# if 'steve' in names:
#     print("steve is in the names!")
# #true - this is case sensitive
# #has to be exact match
# my_answer = input("what is your answer? ")
#
# this is the in operator
# options = ["rock", "paper", "scissors"]
# if my_answer in options:
#     print("that is one of the possible options!")
# else:
#     print(my_answer + " is not one of the possible options!")
    

key = "name"
person = {
    "name": "sean",
    "profession": "Coder",
}

if key in person:
    print(key + " is a valid dictionary key in person object")