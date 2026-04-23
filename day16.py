class modifier:
    __a = "this is private data"
    b = __a


class test(modifier):
    d = 2


obj = test()
print(obj.b)


class accountinfo:

    def setAccount(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def getBalance(self):
        balance = self.__balance
        return balance

    def displayAccount(self):
        
        return f"""
--- Account Info ---
Account Number: {self.__account_number}
Balance: {self.getBalance()}"""


class savingsAccount(accountinfo):

    def setSavingsDetails(self, interest_rate):
        self.__InterestRate = interest_rate

    def calculateInterest(self):
        self.interest = self.getBalance() * self.__InterestRate / 100

    def displaySavingsAccount(self):
        return f"""{self.displayAccount()}
--- Savings Info ---
Interest: {self.interest}"""


class PremiumSavings(savingsAccount):

    def setBonous(self, bonus):
        self.__bonus = bonus

    def calculateTotalBalance(self):
        self.total = self.getBalance() + self.interest + self.__bonus
        return self.total

    def displayPremiumDetails(self):
        return f"""{self.displaySavingsAccount()}
--- Premium Savings Info ---
Bonous:{self.__bonus}
Total Balance:{self.calculateTotalBalance()}"""


obj = PremiumSavings()
obj.setAccount(input("Enter Account Number: "), int(input("Enter Initial Balance:")))
obj.deposit(1000)
obj.setSavingsDetails(float(input("Enter Interest Rate: ")))
obj.calculateInterest()
obj.setBonous(float(input("Enter Bonus: ")))
print(obj.displayPremiumDetails())
