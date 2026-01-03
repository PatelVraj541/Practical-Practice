x = int(input("Enter the number of days after you are returning the book: "))
if x <= 5:
    fine = x * 40
    fineinr = fine / 100
    print(f"The fine to be paid is: ₹{fineinr}")
elif x > 5 and x <= 10:
    fine = (5 * 40) + (x - 5) * 60
    fineinr = fine / 100
    print(f"The fine to be paid is: ₹{fineinr}")
else:
    fine = (5 * 40) + (5 * 60) + (x - 10) * 80
    fineinr = fine / 100
    print(f"The fine to be paid is: ₹{fineinr}")
