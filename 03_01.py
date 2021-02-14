n = int(input("Enter a number = "))

print("Acutal Number = ",n)

rev = 0
while (n!=0):
    rem = n % 10
    n = n // 10
    rev = (rev * 10) + rem

print("Reverse Number = ",rev)
