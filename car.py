class car:
    wheels = 4
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = car("volvo", "XC90")
car2 = car("Honda", "civic")

car1.wheels = 8
print(f"This is a {car1.brand} {car1.model} and it has {car1.wheels} wheels")

print(f"This is a {car2.brand} {car2.model} and it has {car2.wheels} wheels")

#here we can see class variable and instance variable is showing different properties
#car1 wheels we have changed still object of car2 variable is same as before