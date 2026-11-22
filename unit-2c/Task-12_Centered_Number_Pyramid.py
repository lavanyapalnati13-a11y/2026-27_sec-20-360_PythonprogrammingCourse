Centered pyramid of numbers
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print("  " * (n - i) + " ".join(str(x) for x in range(1, 2 * i)))
