# Method Overriding:
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


# Method Overloading (Limited support: for using default parameter values or variable arguments.):

class Calculator:
    def add(self, x, y=0):
        return x + y

calc = Calculator()
print(calc.add(2, 3)) 
print(calc.add(2)) 