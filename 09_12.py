for i in range(1,6):
    for k in range(6,i,-1):
        print(" ",end="")
    for n in range(2,i):
        print("*",end="")
    for m in range(1,i*2):
        print("*",end="")
    print("")

