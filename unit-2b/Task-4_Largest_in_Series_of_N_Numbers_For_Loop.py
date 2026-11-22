 Largest in a series of N numbers using for loop
n = int(input("How many numbers? "))
if n > 0:
    largest = float(input("Enter number: "))
    for i in range(n - 1):
        value = float(input("Enter number: "))
        if value > largest:
            largest = value
    print("Largest =", largest)
else:
    print("Enter at least one number")


