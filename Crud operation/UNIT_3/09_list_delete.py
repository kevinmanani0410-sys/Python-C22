numbers = [10, 20, 30, 40, 50]

x = int(input("Enter value to delete: "))

if x in numbers:
    numbers.remove(x)
    print("After deletion:", numbers)
else:
    print("Value not found")
