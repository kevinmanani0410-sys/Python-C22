file_path = input("Enter a file name: ")
try:
    with open(file_path, "r") as input_file:
        print(input_file.read())
except FileNotFoundError:
    print("File does not exist.")
