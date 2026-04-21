f=open('day16.py','r')
print(f.read())


f=open('day11.py','w')
f.write("this is data")
f.close()


f=open('day11.py','a')
f.write("this is data")
f.close()

f=open('test.py','w')


import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        


