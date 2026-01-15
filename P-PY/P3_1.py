n = input("Enter a number: ")
l = len(n)
n = int(n)
ans = 0
temp = n
while temp > 0:
    digit = temp % 10
    ans += digit ** l
    temp //= 10
if ans == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")