file = open("ex.txt", "w")
file.write("Hello, this is my first file handling example!")
file.close()

file = open("ex.txt", "r")
content = file.read()
print(content)
file.close()
