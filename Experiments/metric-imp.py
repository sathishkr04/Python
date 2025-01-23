while True:
    mtr = int(input("Tell me what i need to convert:\n1-Length\n2-weight\n3-volume\n4-Exit\n Tell me here: "))
    if mtr==1:
        u = float(input("Enter meter value: "))
        print(f"The {u} meters in centimetre is {u*1000}")
    elif  mtr==2:   
        u = float(input("Enter Kilogram value: "))
        print(f"The {u} Kg in gram is {u*1000}")
    elif  mtr==3:   
        u = float(input("Enter liter value: "))
        print(f"The {u}liters in millilitre is {u*1000}")  
    elif mtr==4:
        break     
    else:
        print("Are you a Robot? Invalid Input")