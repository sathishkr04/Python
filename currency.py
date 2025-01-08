while True:
    v = int(input("Lets convert currencies \n 1.USD\n2.EUR\n3.YEN\n4.exit\n Tell me: "))
    if v==4:
        break
    i = float(input("Enter Indian money to convert:"))
    if v==1:
        print(f"The INR to USD of {v} is $ {i*0.012}")
    elif v==2:
        print(f"The INR to EUR of {v} is: {i*0.0112}")
    elif v==3:
        print(f"The INR to EUR of {v} is:{i*1.84}") 
    else:
        print("Enter valid input")


