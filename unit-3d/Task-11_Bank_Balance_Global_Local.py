balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("After deposit:", balance)

def show_local():
    balance = 500
    print("Local balance:", balance)

deposit(500)
show_local()

print("Actual bank balance:", balance)
