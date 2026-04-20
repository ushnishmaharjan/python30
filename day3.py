print(1 == 1)
print(2 != 2)
print(3 < 5)
print(3 > 0)
print(6 >= 1)
print(7 <= 10)
print(2 == 2 and 1 != 2)
print(2 == 1 or 1 == 1)

logged_in = False
print(not logged_in)

# a=int(input("enter a number"))
# b=int(input("enter 2nd number"))

# print(type(a))
# print("add" ,a+b)
name = "suman"
age = 14
address = "nepal"
output = f"My name is {name} and my age is {age} and i live in {address}"
print(output)

if 1 != 1 and 2 == 2:
    print("data")
    print("i am still in if block")
else:
    print("iam else condition")

print("i am outside if condition")

n = int(input("enter a number "))
if n % 2 == 0:
    print(f"{n} is a even number")

else:
    print(f"{n} is a odd number")

name = input("enter your name")
address = input("enter your address")
age = input("enter your age")

print(f"My name is {name} , age is {age} and address is {address}")

if 11 == 2:
    print("this is if condition")
elif 2 == 1:
    print("this is elif condition")
elif 12 == 1:
    print("this is elif condition")
else:
    print("this is else condition")

n = float(input("enter your grade"))
if n >= 3.8 and n <= 4.0:
    print("A+")
elif n >= 3.6 and n <= 3.8:
    print("A")
elif n >= 3.2 and n <= 3.6:
    print("B+")
elif n >= 3.0 and n <= 3.2:
    print("B")
elif n >= 2.8 and n <= 3.0:
    print("C+")
elif n >= 2.6 and n <= 3.0:
    print("C")
elif n >= 2.0 and n <= 2.6:
    print("D+")
elif n >= 1.0 and n <= 2.0:
    print("D")
else:
    print("NG")

gender = "M"
