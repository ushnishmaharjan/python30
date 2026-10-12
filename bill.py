class customer():
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def display_customer_info(self):
        return f'''Customer Name: {self.name}
        Address: {self.address}
        Phone: {self.phone}'''

class purchase():
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    def calculate_total(self):
        return self.quantity * self.price

    def display_purchase_info(self):
       return f'''Item Name: {self.item_name}
        Quantity: {self.quantity}
        Price: {self.price}
        Total Cost: {self.calculate_total()}'''
    
obj1 = customer(
    name= input("customer name: "),
    address= input("customer address: "),   
    phone= input("customer phone: ")
    
)
obj2 = purchase(
    item_name=input("item name: "),
    quantity=int(input("quantity: ")),
    price=float(input("price: "))
)

if item_name ==2 :
    

print(obj1.display_customer_info())
print(obj2.display_purchase_info())

