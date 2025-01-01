name = "sean"
#with .format
welcome_message = "hello {} welcome to python 101".format(name)

print(welcome_message)

#old way
welcome_old = f"hello %s welcome to python 101" % name

#new way

welcome_fstring = f"hello {name} welcome to python 101"
print(welcome_fstring)