""" Bubble Sort Index """
x = [1,4,3,2]
x_b = x.copy()
x_in = []
for i in range(len(x)):
    for j in range(len(x)-1):
        if x[j] > x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
            # print(x)

for k in range(len(x)):
    c = x_b.index(x[k])
    x_in.append(c)
print(x_in)

