def calculate(a, b):
    return a + b, a - b, a * b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

s, d, m = calculate(x, y)

print("Addition =", s)
print("Subtraction =", d)
print("Multiplication =", m)
