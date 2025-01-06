animals =  ["dog","cat","mouse","bird"]

for animal in enumerate(animals):
    print(animal)
#prints out 0 indexed tuple

for index, animal in enumerate(animals):
#    if index % 2 ==0:
#        continue
#   print(animal)
    print(f"{index+1}.\t{animal}")