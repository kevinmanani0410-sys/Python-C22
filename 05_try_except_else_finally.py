try:
    input_num = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input.")
else:
    print("Square:", input_num * input_num)
finally:
    print("Program finished.")
