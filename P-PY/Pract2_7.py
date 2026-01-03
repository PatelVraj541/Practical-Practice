num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
numbers = [num1, num2, num3]
odd_numbers = [n for n in numbers if n % 2 != 0]
odd_count = len(odd_numbers)
print(f"Count of odd numbers: {odd_count}")
if odd_count > 0:
    max_odd = max(odd_numbers)
    print(f"Maximum odd number: {max_odd}")
else:
    print("No odd numbers found")