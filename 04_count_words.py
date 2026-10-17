with open("sentence.txt", "w") as sentence_file:
    sentence_file.write("Python is easy to learn")
with open("sentence.txt", "r") as sentence_file:
    sentence = sentence_file.read()
word_list = sentence.split()
print("Number of words:", len(word_list))
