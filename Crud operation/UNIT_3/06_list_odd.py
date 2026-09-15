numbers = [2, 5, 8, 11, 14, 17]
odd = []

for x in numbers:
    if x % 2 != 0:
        odd.append(x)

print("Odd numbers =", odd)
