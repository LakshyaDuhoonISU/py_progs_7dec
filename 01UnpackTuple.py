#wap to unpack a tuple in several variables
a=(1,2,"abc",[3,4],"xyz")
'''b=a[0]
c=a[1]
d=a[2]
e=a[3]
f=a[4]
print(b,c,d,e,f)
'''
for i in a:
    b=i
    print(b)
