numbers = {10, 20, 30, 40}

print("Original set:", numbers)

print("Is 20 present?", 20 in numbers)

numbers.add(50)
print("After add:", numbers)

numbers.remove(30)
print("After remove:", numbers)

numbers.discard(60)
print("After discard:", numbers)
