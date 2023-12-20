'''#wap to add a tuple to a list
a=[1,3,5,6]
b=(67,46,78)
a.extend(b)
print(a)'''

'''#wap to find the size of a tuple using len() method
a=(66,77,88,'car','roy',87.65)
print(len(a))'''

'''#wap to create a list of tuples from given list having number and its cube in each tuple
c=[2,3,4,5,6]
a=[]
for i in c:
    a.append((i,i**3))
print(a)'''

#wap to add a list to a tuple
a=(1,2,3,4)
b=list(a)
b=b+[5,6,7,8]
a=tuple(b)
print(a)

#wap to 