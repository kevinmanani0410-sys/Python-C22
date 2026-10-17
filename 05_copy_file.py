with open("source.txt", "w") as data_file:
    data_file.write("Welcome to Python practical.")
with open("source.txt", "r") as data_file:
    file_data = data_file.read()
with open("copy.txt", "w") as data_file:
    data_file.write(file_data)
print("File copied successfully.")
