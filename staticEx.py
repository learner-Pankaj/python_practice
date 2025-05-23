class MathUtils:
    @staticmethod
    def add(x, y):
        return x+y
    
sum = MathUtils.add(4,5)
print("Sum = ", sum)

#we use static methos to not to make object of the class, we can use it by using class name with dot operator access its attibutes