#code for factorial
'''num = int(input("Enter a Number : "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial*i

print(factorial)'''


#create a function to calculate factorial of a number
def calcFact(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    return fact

number = int(input("Enter a number : "))
factorial = calcFact(number)
print(factorial)