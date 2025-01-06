#open files with context managers
with open('readme.txt', 'r') as file:
    #print(file.read())
    #want to store in a var?
    content = file.read()
#with means its open only in this indentation
#aka - its scoped and closes automatically

#assign it to a var to get out of scope
#behind the scenes python closed the file
print("the content is: ", content)