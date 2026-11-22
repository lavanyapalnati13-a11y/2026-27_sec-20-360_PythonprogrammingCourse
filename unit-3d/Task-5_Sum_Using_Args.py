def total(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print("Sum:", total(10, 20, 30, 40))
