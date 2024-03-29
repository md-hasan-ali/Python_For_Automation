class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Polymorphism in action
def animal_sounds(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

animal_sounds(dog)  
animal_sounds(cat)