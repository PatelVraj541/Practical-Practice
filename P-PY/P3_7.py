st = input("Enter a string: ")
digits = 0
upper = 0
lower = 0
for ch in st:
    if ch.isdigit():
        digits += 1
    elif ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Number of digits:", digits)
print("Number of uppercase characters:", upper)
print("Number of lowercase characters:", lower)
