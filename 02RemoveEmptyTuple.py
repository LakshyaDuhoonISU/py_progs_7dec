#wap to remove an empty tuple from a list of tuples
a=[(),(),(","),("a","b"),("a","b","c"),("d")]
'''b=[]
print(a)
for i in a:
    if i!=():
        b.append(i) #as modifying and checking the same list will result in error so another list is created where elements are added
print(b)'''

a=[i for i in a if i!=()] #list comprehension
print(a)
