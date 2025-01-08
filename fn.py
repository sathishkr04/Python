s=str(input("Enter content to fill in devo.txt\n"))
try:
    with open("devo.txt","r+") as f1:
        f1.write("s")
    with open("devo.txt","a+") as f2:
        f2.write("\n New line has been appended")    
except FileNotFoundError as e:
    print(f"File that you have mentioned {e}")
