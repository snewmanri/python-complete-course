#example

class Animal:
    prop1 = {
        'key_1': 'value_1',
        'key_2': 'value_2'
    }
    this_list = ['joe','sam','bob']
    
    _like_this = "this is a private property"
    
the_animal = Animal()

#Class - Property (dictionary type)
print(the_animal.prop1['key_1'])
print(the_animal.this_list[1])

print(Animal.this_list)