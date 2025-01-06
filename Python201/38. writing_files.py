with open('writing_files.txt','w') as file:
    file.write("hello from python 201 2 times")

with open('writing_files.txt','a') as file:
    file.write("\na second line")
    file.write("\n\ttabbed line")


