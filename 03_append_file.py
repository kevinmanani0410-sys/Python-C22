with open("names.txt", "w") as name_file:
    name_file.write("Amit\nNeha\n")
new_name = input("Enter another name: ")
with open("names.txt", "a") as name_file:
    name_file.write(new_name + "\n")
with open("names.txt", "r") as name_file:
    print(name_file.read())
