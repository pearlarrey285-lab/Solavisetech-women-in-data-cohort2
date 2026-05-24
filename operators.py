import math

a = 10
b = 5
print("--- Simple Calculator ---")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")

print("\n--- Area of Shapes ---")
radius = 7
circle_area = math.pi * (radius ** 2)
print(f"Circle Area: {circle_area:.2f}")

length, width = 10, 5
rect_area = length * width
print(f"Rectangle Area: {rect_area}")

base, height = 8, 4
triangle_area = 0.5 * base * height
print(f"Triangle Area: {triangle_area}")

print("\n--- Even or Odd ---")
number = 7
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

print("\n--- Student Grade Percentage ---")
score = 85
total_possible = 100
percentage = (score / total_possible) * 100
print(f"Percentage: {percentage}%")

print("\n--- BMI Calculator ---")
weight_kg = 70
height_m = 1.75
bmi = weight_kg / (height_m ** 2)
print(f"Your BMI is: {bmi:.2f}")

print("\n--- Power & Modulus ---")
print(f"2 to the power of 3 is: {2 ** 3}")
print(f"Remainder of 10 divided by 3 is: {10 % 3}")
