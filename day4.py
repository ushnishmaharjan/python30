data=[]

data=[1,"testing",3,3,5]
print(type(data))
print(len(data))
print(data[0])
data[0]=12
'''
append
insert
extends
concat
'''

#Append
a=[1,2,2,2,3,4,5]
a.append(1)
a.append("testing")

b=[]
b.append("this is list")
print(b)

#Insert
data=["hello","hi",1,2,3]
data.insert(0,"1")

data.insert(60,"new")

print(data)

#extends

a=[1,2,3,4]
b=[5,6,7,8]
c=b.extend(a)
a.extend(b)
print(a)
print(b)
print(c)

#concat

a=[1,2,3,4]
b=[5,6,7,8]
c=a+b
print(a,b)
print(c)


#slicing
data=[1,2,3,4,5,6,7,8]

print(data[0:4])
print(data[:4])
print(data[2:])

print(data[:])

'''
del
remove
pop
clear
'''

data=[1,2,3,4,5,6,7,8]
del data[0]

#remove
data.remove(2)
print(data)

#pop
data=[1,2,3,4,5,6,7,8]
data.pop()

#clear
data.clear()

data=[1,2,3,4,5,6,2,2,2,7,8]
count_data=data.count(2)
print(count_data)
index_data=data.index(3)
print(index_data)

data.reverse()
print(data)

data.sort()
print(data)

data.sort(reverse=True)
print(data)

