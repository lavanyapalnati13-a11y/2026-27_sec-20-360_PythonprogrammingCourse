Demonstrate pass using for and while
print("Using for loop:")
for i in range(1, 6):
    if i == 3:
        pass
    print(i, end=" ")
print("\nUsing while loop:")
i = 1
while i <= 5:
    if i == 3:
        pass
    print(i, end=" ")
    i += 1
