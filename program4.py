#wap to calculate parking charges of a vehicle. Enter the type of vehicle as a character(c=car,b=bus,etc), and no of hours, then calculate charges as given below.
#truck,bus=20rs per hour, car=10rs per hour, scooter,cycle=5rs per hour
'''a=input("Welcome to ABC Parking Lot\nEnter the type of vehicle\n1.Enter 'c' for car\n2.Enter 'b' for bus\n3.Enter 't' for truck\n4.Enter 's' for scooter\n5.Enter 'cycle' for cycle.\n")
if a.lower()=="c":
    b=int(input("Enter number of hours: "))
    print("Your parking charges are:",b*10)
elif a.lower()=="b":
    b=int(input("Enter number of hours: "))
    print("Your parking charges are:",b*20)
elif a.lower()=="t":
    b=int(input("Enter number of hours: "))
    print("Your parking charges are:",b*20)
elif a.lower()=="s":
    b=int(input("Enter number of hours: "))
    print("Your parking charges are:",b*5)
elif a.lower()=="cycle":
    b=int(input("Enter number of hours: "))
    print("Your parking charges are:",b*5)
else:
    print("Invalid vehicle type!")'''

#modify the program to read hours and minutes of checkout and checkin times and calculate charges based on the difference 
#rate till 3 hours- truck/bus=20,car=10,cycle/scooter=5
#rate after 3 hours- truck/bus=30,car=20,cycle/scooter=10
a=input("Welcome to ABC Parking Lot\nEnter the type of vehicle\n1.Enter 'c' for car\n2.Enter 'b' for bus\n3.Enter 't' for truck\n4.Enter 's' for scooter\n5.Enter 'cycle' for cycle.\n")
if a.lower()=="c":
    b=float(input("Enter check in time(24h format): "))
    c=float(input("Enter check out time(24h format): "))
    d=c-b
    print("\n\t\t\tParking Receipt")
    print("\nType of vehicle\tCheck In Time:\tCheck Out Time:\tTotal time:\tParking Charges")
    if d>3:
        e=d-3
        f=d-e
        print("Car\t\t",b,"\t\t",c,"\t\t",round(d,3),"\t\t",(e*20)+(f*10))
    else:
        print("Car\t\t",b,"\t\t",c,"\t\t",round(d,3),"\t\t",d*10)
elif a.lower()=="b":
    b=float(input("Enter check in time: "))
    c=float(input("Enter check out time: "))
    d=c-b
    print("\n\t\t\tParking Receipt")
    print("\nType of vehicle\tCheck In Time:\tCheck Out Time:\tTotal time:\tParking Charges")
    if d>3:
        e=d-3
        f=d-e
        print("Bus\t",b,"\t",c,"\t",round(d,3),"\t",(e*30)+(f*20))
    else:
        print("Bus\t",b,"\t",c,"\t",round(d,3),"\t",d*20)
elif a.lower()=="t":
    b=float(input("Enter check in time: "))
    c=float(input("Enter check out time: "))
    d=c-b
    print("\n\t\t\tParking Receipt")
    print("\nType of vehicle\tCheck In Time:\tCheck Out Time:\tTotal time:\tParking Charges")
    if d>3:
        e=d-3
        f=d-e
        print("Truck\t",b,"\t",c,"\t",round(d,3),"\t",(e*30)+(f*20))
    else:
        print("Bus\t",b,"\t",c,"\t",round(d,3),"\t",d*20)
elif a.lower()=="s":
    b=float(input("Enter check in time: "))
    c=float(input("Enter check out time: "))
    d=c-b
    print("\n\t\t\tParking Receipt")
    print("\nType of vehicle\tCheck In Time:\tCheck Out Time:\tTotal time:\tParking Charges")
    if d>3:
        e=d-3
        f=d-e
        print("Scooty\t",b,"\t",c,"\t",round(d,3),"\t",(e*10)+(f*5))
    else:
        print("Truck\t",b,"\t",c,"\t",round(d,3),"\t",d*5)
elif a.lower()=="cycle":
    b=float(input("Enter check in time: "))
    c=float(input("Enter check out time: "))
    d=c-b
    print("\n\t\t\tParking Receipt")
    print("\nType of vehicle\tCheck In Time:\tCheck Out Time:\tTotal time:\tParking Charges")
    if d>3:
        e=d-3
        f=d-e
        print("Cycle\t",b,"\t",c,"\t",round(d,3),"\t",(e*10)+(f*5))
    else:
        print("Cycle\t",b,"\t",c,"\t",round(d,3),"\t",d*5)
else:
    print("Invalid vehicle type!")
