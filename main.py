file = open("text.txt")
contents = file.read()
print(contents)
file.close()

# same code but with new keyword -> we do not have to type 'file2.close()
with open("text2.txt", mode="w") as file2:
    file2.write("I'm here again!")

with open("text.txt", mode="a") as file:
    file.write("\nDanko!")
