#nested tuple
#wap to print name of topper and his/her marks in 4 subjects wherein the marks are specified as a list in the tuple topper
a=input(("Enter Name of student: "))
a1=[a]
highest=0
total=0
topper=[]
for i in range(4):
    b=float(input(f"Enter {i+1} subjects marks: "))
    a1.append(b)
print(a1)
c=input(("Enter Name of student: "))
a2=[c]
for i in range(4):
    b=float(input(f"Enter {i+1} subjects marks: "))
    a2.append(b)
print(a2)
d=input(("Enter Name of student: "))
a3=[d]
for i in range(4):
    b=float(input(f"Enter {i+1} subjects marks: "))
    a3.append(b)
print(a3)
tuple1=[a1,a2,a3]
print(tuple1)
for i in tuple1:
    total=sum(i[1:])
    if total>highest:
        highest=total
        topper=i
print(f"Name of topper: {topper[0]}\nMarks:{topper[1],topper[2],topper[3],topper[4]} \nTotal marks: {highest}")

'''a=[("ABC",57,78,65,78),("DEF",50,67,51,67),("XYZ",90,95,85,98)]
marks=0
highest=0
b=[]
for i in a:
    marks=0
    marks=i[1]+i[2]+i[3]+i[4]
    if marks>highest:
        highest=marks
        b=i
print(b)
print("Name of Topper:",b[0],"\nMarks:",b[1],b[2],b[3],b[4])'''