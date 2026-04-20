#for i in "broadway":
#    print(i)
#for i in [1,2,3,4,5,6,7,8,9]:
#    print(i)
#data= {
#    "name":"Ram",
#    "age":"67",
#    "address":"Nepal"
#}
#for i in data:
#    print(f'{i}={data[i]}')
#for i in [1,2,3,4,5,6,7,8,9]:
#    if i%2==0:
#        print(f'{i} is even')
#    else:
#        print(f'{i} is odd')

#print("----------" * 10)
#for i in range(1,100,1):
#    if i%2==0:
#        print(f'{i} is even')
#    else:
#        print(f'{i} is odd')

a=[1,2,"hello","test",1.2,"broadway"]
a=[1,"hi"]
for i in a:
    if type(i)==str:
        print(i)

a=[1,2,"hello","test",1.2,"broadway"]
a=[1,"hi"]
for i in a:
    if isinstance(i,str):
        print(i)


#nested loop
for i in [1,4]:
    for j in [1,4]:
        print(i,j)

count=0
a=["program"]
for i in a.lower():
    if i==["a","e","i","o","u"]:
        count+=1
