# try:
#     print("trying 1/0")
#     total = 1 / 0
#     print("this will not show up")
#     #this will not execute
#     #cant divide by 0
# except Exception:
#     #this wil execute
#     print("exception was caught")
#     total = 0
    
# print(total)

num = input("what is a number? ")
try:
    num = int(num)
except Exception:
    num = "NOT A NUMBER!"
    
print(num)