#example

class Animal:
    prop1 = {
        'key_1': 'value_1',
        'key_2': 'value_2'
    }
    this_list = ['joe','sam','bob']
    
    def add_name(self,name):
        self.this_list.append(name)
        return self.this_list
    
    def remove_name(self,name):
        self.this_list.remove(name)
        return self.this_list
    
    _like_this = "this is a private property"
    
    #self is the same as 'this' in javascript
    #or -> in php
    def this_is_a_method(self):
        print(self.this_list)
    
    #when you use property syntax
    #you dont have to use () when calling
    @property 
    def get_sam(self):
        return self.this_list[1]


the_animal = Animal()
# the_animal.this_is_a_method()
# sam = the_animal.get_sam
# print("the dudes name is", sam)

the_animal.add_name("rhubarb")
the_animal.remove_name("bob")
print(the_animal.this_list)