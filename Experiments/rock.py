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