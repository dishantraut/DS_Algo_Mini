n = int(input("Enter a number = "))

len_ = 0
while (n!=0):
    n = n // 10
    len_ += 1

print("Lenght = ",len_)
