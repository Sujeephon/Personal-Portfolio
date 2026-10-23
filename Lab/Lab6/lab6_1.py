def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division result and handle division by zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b


# Challenge: ฟังก์ชันยกกำลัง
def power(base, exponent=2):
    """Return the base raised to the given exponent."""
    return base ** exponent

while True:
    print("\n========== Simple Calculator ==========")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")

    choice = input("Choose an operation (1-6): ")

    if choice == "6":
        print("Exiting calculator.")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)

        elif choice == "2":
            result = subtract(num1, num2)

        elif choice == "3":
            result = multiply(num1, num2)

        elif choice == "4":
            result = divide(num1, num2)

        print(f"Result: {result}")

    elif choice == "5":
        base = float(input("Enter base: "))

        exponent_input = input(
            "Enter exponent (press Enter for default = 2): "
        )

        if exponent_input == "":
            result = power(base)
        else:
            exponent = float(exponent_input)
            result = power(base, exponent)

        print(f"Result: {result}")

    else:
        print("Invalid choice! Please choose 1-6.")