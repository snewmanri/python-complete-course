class Animal:
    fur_color = "Orange"
    
    def speak(self):
        raise NotImplementedError
    
    def eat(self):
        print("i am eating yum!")
    
    def chase(self, animal="gazelle"):
        print("im chasing a", animal)
    
class HouseCat(Animal):
    def speak(self):
        print("meow")
        
    def eat(self):
        super().eat()
        print("i'm eating salmon")
        
    def chase(self,animal):
        super().chase(animal)
        print(animal, "was caught")

cat = HouseCat()
cat.chase("mouse")