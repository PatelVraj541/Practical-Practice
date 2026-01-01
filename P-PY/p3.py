radius = float(input("Enter radius of the cylinder (cm): "))
height = float(input("Enter height of the cylinder (cm): "))
pi = 3.14159
volume = pi * radius * radius * height
surface_area = 2 * pi * radius * radius + 2 * pi * radius * height
print("\n" + "-" * 45)
print("CYLINDER MEASUREMENT RESULTS")
print("-" * 45)
print(f"{'Radius':20}: {radius} cm")
print(f"{'Height':20}: {height} cm")
print(f"{'Volume':20}: {volume:.2f} cubic cm")
print(f"{'Surface Area':20}: {surface_area:.2f} sq. cm")
print("-" * 45)