def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

n = int(input("Enter number: "))
temp = n
total = 0

while n!= 0:
    digit = n % 10
    total += factorial(digit)
    n //= 10

if temp == total:
    print("Strong")
else:
    print("Not Strong")