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

p1 = Person('Pankaj', 26)

print(p1.name)
print(p1.age)