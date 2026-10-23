num = input("What is your favorite number? : ")
num = int(num)

if num < 0:
    sign = "negative"
elif num > 0:
    sign = "positive"
else:
    sign = "zero"

if num % 2 == 0:
    parity = "even"
else:
    parity = "odd"

print(f"Your favorite number is {sign} and {parity}.")
    