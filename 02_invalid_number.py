try:
    user_age = int(input("Enter your age: "))
    print("Your age is", user_age)
except ValueError:
    print("Please enter a valid integer.")
