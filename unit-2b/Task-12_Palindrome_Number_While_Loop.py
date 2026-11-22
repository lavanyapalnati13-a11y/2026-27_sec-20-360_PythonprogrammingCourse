Palindrome number using while loop
n = int(input("Enter a number: "))
temp = n
reverse = 0
while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10
if n >= 0 and n == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")


