num = int(input('Enter a Positive number = '))
sum = 0
print('\nProper divisors of', num, 'are = ', end='')
for i in range(1, (num//2)+1):
    if num % i == 0:
        sum = sum + i
        print(i, ',', end='')
print("\n")
print('Sum of Proper Divisors of', num, 'is = ', sum)
print("")
if num == sum:
    print(num, 'is a Perfect Number.')
else:
    print(num, 'is not a Perfect Number.')
