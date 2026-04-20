class test:
    a = 100
    b = 12


obj = test()
obj.data = "this is obj attrs"

obj1 = test()
obj1.data = "this is obj1 attrs"

obj2 = test()


a = 1
b = 1

print(obj == obj1)


print(obj)
print(obj1)
print(obj2)
print(obj.data)
print(obj1.data)


class Math:
    a = 100
    b = 12

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def result(self):
        return {"add": self.add(), "sub": self.sub()}


obj = Math()
print(obj.result())

print("--------" * 13)


class String_Test:
    data = "hello"

    def __str__(self):
        return f"{self.data} this is from str func"


obj = String_Test()
print(obj)

print("--------" * 13)


class constTest:
    def __init__(self, a, b, c):
        print("this is from cons")
        self.a = a
        self.b = b
        self.c = c
    def add(self):
        print(self.a + self.b + self.c)




obj = constTest(1, 2, 3)
obj.add()
