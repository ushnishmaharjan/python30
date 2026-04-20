class modifier():
    __a="this is private data"
    b=__a

class test(modifier):
    d=2

obj=test()
print(obj.b)



class accountinfo():

    def setAccount(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        pass

    def getBalance(self):
        balance = self.__balance
        return balance

    def displayAccount(self):
        1