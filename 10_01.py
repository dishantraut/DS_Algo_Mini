""" Bubble Sort Algorithm """
x = [2,3,4,55,6,7,1,4,3,2]

print("Ascending Order Sort")
for i in range(len(x)):
    for j in range(len(x)-1):
        if x[j] > x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
            print(x)

print("\n\n")

print("Descending Order Sort")
for i in range(len(x)):
    for j in range(len(x)-1):
        if x[j] < x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
            print(x)

