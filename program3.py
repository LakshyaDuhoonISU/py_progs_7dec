#wap to unzip a list of tuples into individual lists
a=[(1,2),(),(","),("a","b"),("a","b","c"),("d")]
for i in a:
    if i!=():
        b=i
        print(b)

