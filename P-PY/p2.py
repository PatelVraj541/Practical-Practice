m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"
print("\n" + "-" * 40)
print("STUDENT RESULT")
print("-" * 40)
print(f"{'Total Marks':15}: {total} / 500")
print(f"{'Percentage':15}: {percentage:.2f}%")
print(f"{'Grade':15}: {grade}")
print("-" * 40)