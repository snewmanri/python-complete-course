class Animal:
    #fur_color = "Orange"
    #dunder methods = double underscore
    #also called magic methods
    
    #this will automatically execute
    #if you dont provide param it throws error
    
    animal_type = "Unknown"
    
    def __init__(self, fur_color):
        self.fur_color = fur_color
        pass
    
    def speak(self):
        raise NotImplementedError
    
    def eat(self):
        print("i am eating yum!")
    
    def chase(self, animal="gazelle"):
        print("im chasing a", animal)
        
    def get_fur_color(self):
        print("getting fur color:", self.fur_color)
    
class HouseCat(Animal):
    
    def __init__(self, fur_color):
        #this does super method to assign fur color
        #aka super lets you call parent methods
        super().__init__(fur_color)
        #then this is new overrides
        print("fur color has been assigned to class object")
        self.animal_type = "House Cat"
        print(self.animal_type)
    
    def speak(self):
        print("meow")
        
    def eat(self):
        #this calls method of parent class
        super().eat()
        print("i'm eating salmon")
        
    def chase(self,animal):
        super().chase(animal)
        print(animal, "was caught")

cat = HouseCat("Orange")
cat.get_fur_color()

dog = Animal("black")
dog.get_fur_color()