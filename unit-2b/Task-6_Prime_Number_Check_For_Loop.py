Prime number using for loop (1 to 100)
n = int(input("Enter a number (1 to 100): "))
is_prime = n >= 2
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")
