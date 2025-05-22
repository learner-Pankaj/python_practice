#this is the simple way to crate class and provide attributes
'''class Person:
    name = 'Pankaj'
    age = 26

p = Person
print(p.name)
print(p.age)'''

#creating class with constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old and my salary is {self.salary}")
    
p1 = Person('Pankaj', 26)
p1.greet()
print(p1.name)
print(p1.age)

e1 = Employee('Pankaj', 26, 1234567)
e1.greet()
