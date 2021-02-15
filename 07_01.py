n = int(input("Enter a number = "))
temp_n = n

rev = 0
while (n!=0):
    rem = n % 10
    n = n // 10
    rev = (rev * 10) + rem
    
if rev == temp_n:
    print("Palindrome Number")
else:
    print("Not Palindrome")
