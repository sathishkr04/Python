# currency conversion of INR to other types

def currency():
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

# unit conversion Metric to Imperial 
def unit():
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

# Rock Paper Scissors
def rock():
    import random
    while True:
        kappal = int(input("Velayadalama:\n1-kallu\n2-kakitham\n3-kathiri\n4-podhum bhaa\n nee choose panu:"))
        if kappal==4:
            break
        n = random.randint(1, 3)  
        print("kuttappan chose: ",n)
        if n == kappal:
            print("neeyu nanum onnu gandhi porandha mannu")
        elif (n==1 and kappal==3) or  (n==3 and kappal==2)  or (n==2 and kappal==1):
            print("Kuttappan wins")
        else:
            print("Nee win") 

# File Handling 

def filehandling():
    new_content = input("Enter your content : ")
    try:
        with open("devo.txt","w") as file:
            file.write(f"{new_content}\n")
            append_content = input("Enter your content : ")
        with open("devo.txt","a") as file1:
            file1.write(f"{append_content}\n")
        with open("images.jpeg", "rb") as img:
            with open("image.jpeg", "wb") as img1:
                for i in img:
                    img1.write(i)    
                else:
                    with open("images.jpeg", "rb") as img:
                        binary_data = img.read()  # Read the binary content
                        print("Image copied successfully to 'image.jpeg'.")

    except PermissionError as per:
        input(f"Permission error Occured : {per}")
    except FileNotFoundError as fn:
        input(f"File not found error occured : {fn}")
    
    
    
# flames
def flames():
    ladka = input("Teri Hero:")
    ladki = input("Meri Jaan:")
    if(ladka==ladki):
        print("Idhu vanavil kootam, Epadithano two different name venum")
    for ltr in ladka:
        if ltr in ladki:
            ladka = ladka.replace(ltr, "", 1)
            ladki = ladki.replace(ltr, "", 1)
    remaining_count = len(ladka) + len(ladki)
    current_index =0 
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(flames) > 1:
        index = (remaining_count + current_index - 1) % len(flames)
        flames.remove(flames[index])
        current_index = index
    print(flames[0]) 

# Payroll
def payroll():
    role_input = input("Enter the role: hr manager others  ")
    if role_input == "others":
        gen_input = input("Enter the gender: male female   ")
    salary_1 = 10000
    salary_2 = 9500
    if role_input == "hr":
        pay = salary_1*0.25 
        tax_val = pay*0.03
        tot_pay = (pay+salary_1) - tax_val
        print("The HR's pay is ",tot_pay)
    elif role_input == "manager":
        pay = salary_2*0.25 
        tax_val = pay*0.03
        tot_pay = (pay+salary_2) - tax_val
        print("The Manager's pay is ",tot_pay)
    elif role_input == "others" and gen_input =="male":
        pay = (salary_1*0.10) + salary_1
        print("The others's male staff pay is ",pay)
    elif role_input == "others" and gen_input =="female":
        pay = (salary_2*0.12) + salary_2
        print("The others's female staff pay is ",pay)
    else:
        print("Enter valid role")

