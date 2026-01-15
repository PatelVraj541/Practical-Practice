st = input("Enter a string: ")
i = int(input("Enter index to remove: "))
if i < 0 or i >= len(st):
    print("Invalid index")
else:
    result = st[:i] + st[i+1:]
    print("String after removing character:", result)
