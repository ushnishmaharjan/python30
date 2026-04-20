class ATM():
    def __init__(self):
        self.balance = 10000


    def withdraw(self,amount):
        if amount>self.balance:
            return "Amount is greater than current balance"
        self.balance = self.balance - amount
        return f'{amount} is withdraw and current balance is {self.current_balance()}'

    def deposit(self, amount):
        if amount<0:
            return "Number must be positive"
        self.balance = self.balance + amount
        return f'{amount} is deposit and current balance is {self.current_balance()}'


    def current_balance(self):
        return self.balance

obj = ATM()
print(obj.deposit(1000))
print(obj.withdraw(200))
print(obj.withdraw(20000))
print(obj.deposit(-1000))


class order():
    def __init__(self ,name, items):
        self.total=0
        if  isinstance(items , list):
            for i in items.value:
                self.total= self.total + i["price"]
        else :
            print("item must be in list")
        

items=[
    {
        "items":"Apple",
        "price": 50
    },
    {
        "items":"Iphone",
        "price": 500000
    },
    {
        "items":"Mac",
        "price": 50000
    },
    {
        "items":"pen",
        "price": 10
    }
]
obj=order()
print

class parent():
    data="broadway"

    def add(self):
        return "this is method from parent class"

class child(parent):
    a=100

odj=child()
print(obj.data)
print(obj.add())

