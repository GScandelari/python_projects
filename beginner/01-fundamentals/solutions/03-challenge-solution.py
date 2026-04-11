# ============================================================
# beginner/01-fundamentals/solutions/03-challenge-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Command-line Calculator
# ----------------------------------------------------------
# APPROACH: Read two floats and an operator. Use if/elif to
# branch. Guard division by zero BEFORE dividing.

def calculator_demo(a, op, b):
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("Error: division by zero is not allowed.")
            return
        result = a / b
    else:
        print(f"Unknown operator: {op}")
        return
    print(f"{a} {op} {b} = {result:.4f}")

calculator_demo(12.0, "*", 7.5)   # 12.0 * 7.5 = 90.0000
calculator_demo(9.0,  "/", 0)     # Error: division by zero


# ----------------------------------------------------------
# Exercise 2 — BMI Calculator
# ----------------------------------------------------------
# APPROACH: Apply the formula, then use if/elif to map the
# value to a WHO category. Check narrower ranges first.

def bmi_demo(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal weight"
    elif bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"
    print(f"Your BMI   : {bmi:.2f}")
    print(f"Category   : {category}")

bmi_demo(70, 1.75)   # BMI 22.86 — Normal weight
bmi_demo(50, 1.75)   # BMI 16.33 — Underweight


# ----------------------------------------------------------
# Exercise 3 — Temperature Converter
# ----------------------------------------------------------
# APPROACH: Read the choice as a string ("1" or "2"). Branch
# on the choice string — no need to convert to int first.

def convert_demo(choice, value):
    print("Temperature converter")
    print("1 - Celsius to Fahrenheit")
    print("2 - Fahrenheit to Celsius")
    print(f"Your choice: {choice}")
    if choice == "1":
        converted = (value * 9 / 5) + 32
        print(f"{value:.2f} C = {converted:.2f} F")
    elif choice == "2":
        converted = (value - 32) * 5 / 9
        print(f"{value:.2f} F = {converted:.2f} C")
    else:
        print("Invalid choice. Please enter 1 or 2.")
    print()

convert_demo("1", 100)   # 100.00 C = 212.00 F
convert_demo("2", 32)    # 32.00 F = 0.00 C
convert_demo("9", 0)     # Invalid choice
