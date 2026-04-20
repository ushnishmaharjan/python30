a = ["sudan", "bhandari", 26, 9802130]
data = {"name": "sudan", "surname": "bhandari", "age": 26, "name": "hari"}
print(data)
print(len(data))

print(type(data))

data["age"] = 100
data["number"] = 6000

data.update({"name": "suman", "number1": 980, "address": "nepal", "surname": "testing"})
print(data)
data2 = {
    "name": "suman",
    "number1": 980,
    "address": "nepal",
    "surname": "testing",
    "numbrer": 6000,
    "age": 100,
}

a = data2.keys()
print(data2.values())


# del
del data2["age"]
print(data2)

# pop
data2.pop("name")

# popitem
data2.popitem()
print(data2)


# clear
data2.clear()

print(data2)
data2 = {
    "name": "suman",
    "number1": 980,
    "address": "nepal",
    "surname": "testing",
    "numbrer": 6000,
    "age": 100,
}
number = data2.get("numbers", "key not found")
num = data2.get("numbers")
print(num, number)
if num:
    print(" ")
else:
    print("key not found")

data = {
    "phone":{
        "ntc":"9844",
        "ncell":{
            "type":'prepaid',
            "balance":1456
        }
    }
}
print("........." * 10)
user_info = {
    "name": "Hari",
    "phone": [
        {"type": "NTC",
         "number": "9844"
        }, 
        {"type": "NCELL",
         "number": "980"
        }
    ],
}
name = user_info["name"]
phone = user_info["phone"]
a = phone

type = a[0]["type"]
number = a[0]["number"]

print(f"{name},  {type}, number is , {number}")
type = a[1]["type"]
number = a[1]["number"]

print(f"{name},  {type}, number is , {number}")

