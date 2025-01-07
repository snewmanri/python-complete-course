num = input("enter a number: ")
num2 = input("enter a second number: ")
try:
    num = int(num)
    num2 = int(num2)
    total = num / num2
except ValueError:
    print("num or num2 were not valid numbers")
except ZeroDivisionError:
    print("num2 cannot be 0")
except Exception as e:
    print("Exception was caught")
    print(type(e))
#python will find the right type of exception
    
print(num)