a=(1,2,3,4,5)
print(type(a))

print(a)
b=list(a)
b[0]=100
print(b)
a=tuple(b)
print(a)


#set
a=[1,2,3,3,1,1,2]
a.remove(1)

a={1,1,1,1,1,"hello",2,"hi"}
print(type(a))

print(a)

print("--------"*10)

def test():
    a=100
    b=11
    add=a+b
    return add,a,b

print(test())

def test1():
    a=11
    b=11
    add=a+b
    return (add,a,b)

print(test1())

def testing():
    a=[1,2,3,4,5,6]
    global data
    data=100
    return a
print(testing())
print(data)

def add_list():
    a=[1,2,3,4,5,6]
    add=0
    for i in a:
        add=add+i
    
    return add


