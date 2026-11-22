Hollow diamond pattern of stars
n = int(input("Enter number of rows in upper half: "))
for i in range(1, n + 1):
    if i == 1:
        print(" " * (2 * (n - i)) + "*")
    else:
        print(" " * (2 * (n - i)) + "*" + " " * (4 * i - 5) + "*")
for i in range(n - 1, 0, -1):
    if i == 1:
        print(" " * (2 * (n - i)) + "*")
    else:
        print(" " * (2 * (n - i)) + "*" + " " * (4 * i - 5) + "*")

