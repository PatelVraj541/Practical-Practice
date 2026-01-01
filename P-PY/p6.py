P = float(input("Enter Principal Amount (P): "))
R = float(input("Enter Rate of Interest (R in %): "))
T = float(input("Enter Time Period (T in months): "))
SI = (P * R * T) / 100
Total = P + SI
print("\n****** Interest Calculation ******")
print("Principal Amount : ₹", P)
print("Rate of Interest : ", R, "%")
print("Time Period      : ", T, "months")
print("Simple Interest  : ₹", SI)
print("Total Amount     : ₹", Total)
