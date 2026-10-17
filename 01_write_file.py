message = input("Enter a message: ")
with open("message.txt", "w") as output_file:
    output_file.write(message)
print("Message saved.")
