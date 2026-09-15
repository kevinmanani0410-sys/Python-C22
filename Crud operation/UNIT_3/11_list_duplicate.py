numbers = [2, 4, 2, 6, 4, 8, 2]
new_list = []

for x in numbers:
    if x not in new_list:
        new_list.append(x)

print("Without duplicates:", new_list)
