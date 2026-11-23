subjects = {
    "Python": 90,
    "Maths": 85,
    "English": 88
}

print("Keys:")
for key in subjects:
    print(key)

print("Values:")
for value in subjects.values():
    print(value)

print("Items:")
for key, value in subjects.items():
    print(key, ":", value)
