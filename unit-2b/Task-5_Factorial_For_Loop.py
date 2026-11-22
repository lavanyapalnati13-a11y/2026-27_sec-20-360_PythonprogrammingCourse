Factorial using for loop
n = int(input("Enter a non-negative number: "))
fact = 1
if n < 0:
    print("Factorial is not defined")
else:
    for i in range(1, n + 1):
        fact *= i
    print("Factorial =", fact)

