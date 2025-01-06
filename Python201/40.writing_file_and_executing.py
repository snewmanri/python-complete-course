filename = input("whats the filename? ")
content = input("enter the content ")

with open(filename, 'w') as file:
    file.write(content)
    
open_file = input("would you like to read this file? ")
if open_file in ['y','n']:
    if open_file == 'y':
        with open(filename,'r') as file:
            print(file.read())