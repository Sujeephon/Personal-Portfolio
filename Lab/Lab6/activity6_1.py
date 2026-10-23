def is_positive_negative_zero(num):
    """
    Check whether a number is positive, negative, or zero.
    """
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def is_even_odd(num):
    """
    Check whether a number is even or odd.
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("=== Number Classifier ===")

number = int(input("Enter an integer: "))

sign = is_positive_negative_zero(number)
parity = is_even_odd(number)

print(f"\nNumber: {number}")
print(f"Type: {sign}")
print(f"Parity: {parity}")