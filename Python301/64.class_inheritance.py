#this is an interface
class Animal:
    fur_color = "Orange"
    
    def speak(self):
        print("rawr")
    
    def eat(self):
        pass
    
    def chase(self):
        pass
    
#extend the animal class
class Tiger(Animal):
    #overriding methods
    def speak(self):
        print("theyre grrreat")

class HouseCat(Animal):
    fur_color = "black"
    def speak(self):
        print("meow")

tiger = Tiger()
tiger.speak()
cat = HouseCat()
cat.speak()
print(cat.fur_color)