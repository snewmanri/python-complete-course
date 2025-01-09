#generator is a way to deal with numbers individually 
#instead of having millions of things in memory at once

#not technically a generator but similar
#for this its doing things without storing in my memory
#this is proper way to use (dont store in list)
#good for disposable code on large datasets
def my_generator():
    for num in range(50):
        yield num ** num

#this is just returning a reference to the generator        
#all_numbers = my_generator()
#print(all_numbers)

#instead you can cast this as a list
#with list you can save them for later
all_numbers = list(my_generator())
print(all_numbers)


#big num is your iterable
#my_generator is the generator function defined above
#here you're not saving for later        

#for big_num in my_generator():
#    print(big_num)

total = list(range(50))
print(total)

#generators are one and done
#you have to instantiate a new one for each time