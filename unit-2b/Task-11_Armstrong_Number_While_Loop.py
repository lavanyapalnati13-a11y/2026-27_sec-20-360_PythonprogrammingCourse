Armstrong number (three-digit number) using while loop
n = int(input("Enter a three-digit number: "))
temp = n
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10
if 100 <= n <= 999 and total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
