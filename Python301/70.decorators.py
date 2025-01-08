#decorators are weird and kinda confusing!
#decorator lets you wrap a function in logic
#the decorator is the wrapper logic
#the passed in function can be called anywhere in there
#good if you need set up and clean up

def my_decorator(func):
    def wrapper():
        print("start of original function")
        func()
        print("original function finished")
    return wrapper

#try executing with next line commented out
#also decorator matches function name
@my_decorator
def myFunc():
    print("hi im decorator function!")

myFunc()

#other method is passing function as arg
#dont need this with decorator
# new_func = my_decorator(myFunc)
# new_func()
