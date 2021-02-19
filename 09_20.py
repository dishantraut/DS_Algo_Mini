n = 1
for i in range(1,6):
    for j in range(1,i):
        if n%2 == 0:
            print("0",end="")
        else:
            print("1",end="")
        n += 1
    print("")
