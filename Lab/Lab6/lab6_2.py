# Lab6.2 Part 2: Use the Custom Module and Standard Module

import my_utils
import math
import random


print("=== Greeting ===")
my_utils.greet("Alice")


print("\n=== Prime Number Test ===")
print(f"Is 7 prime? {my_utils.is_prime(7)}")
print(f"Is 10 prime? {my_utils.is_prime(10)}")


print("\n=== Square Root ===")
number = 25
result = math.sqrt(number)
print(f"Square root of {number} = {result}")


print("\n=== Random Number ===")
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")