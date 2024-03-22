class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving")
    
car1 = Car("Toyota", "Camry")
print(car1.brand)
car1.drive()