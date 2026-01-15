x = "Print Only the words that start with s in the given string"
y = x.split()
count = 0
for i in y:
    if i[0].lower() == 's':
        print(i)
        count += 1
print("Total words starting with 's':", count)