for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(1,i):
        print("*",end="")
    print("")

for i in range(1,6):
    for k in range(1,i):
        print(" ",end="")
    for j in range(5,i,-1):
        print("*",end="")
    print("")

#    *
#   **
#  ***
# ****
# ****
#  ***
#   **
#    *