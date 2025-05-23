class Bank:
    __balance = 100000
    def __init__(self):
        pass

    def deposit(self, amnt):
        self.__balance += amnt
        return self.__balance

    def getBalance(self):
        return self.__balance
    
    def withdraw(self, amnt):
        self.__balance -= amnt
        return self.__balance

b1 = Bank()
checkAccount = b1.getBalance()
withdraw = b1.withdraw(20000)
bal = b1.deposit(100000)
print("check Account", checkAccount)
print("Withdrawal ", withdraw)
print("New Balance ", bal)

#this is a class private attributes using example
