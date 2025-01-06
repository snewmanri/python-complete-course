#fuctions in functions a decorator primer lesson
#python can have functions in functions

def thing1(name):
    print("welcome to thing 1 ", name)
    def thing2():
        print("welcome to thing 2 ", name)
    thing2()
    
thing1("joe")

#A function in function is called a decorator

#pythonic scoping - if it doesn't find inside function
#it looks outside of function to find it

#if you have a nested function you can use all parent variables

#nested function also called sub function