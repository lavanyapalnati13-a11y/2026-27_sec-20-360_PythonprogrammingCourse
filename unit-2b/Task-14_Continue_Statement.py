 Demonstrate continue using for and while
print("Using for loop:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
print("\nUsing while loop:")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=" ")
