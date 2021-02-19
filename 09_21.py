# Cross pattern
for i in range(5):
    for k in range(5):
        if (i==k) or (i+k == 5-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
