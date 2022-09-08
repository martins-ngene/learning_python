# To open a file
example = open("../index.html", "w")

# Use "r" to read files, "a" to append new lines, "w" to overwrite file and can also create new files, "r+" to have
# full power

# To check if a file is readable
# print(example.readable())

# To read entire file
# print(example.read())

# To return an array of the files content
# array_of_lines = example.readlines()

# To loop through array
# for item in array_of_lines:
#     print(item)

# To read a line by line
# print(example.readline())
# print(example.readline())

# Append new line into file
# write_example = example.write("\n\nLorem Ipsum Dolo 7")

# Overwrite file
overwrite_example = example.write("<p>Hello World</p>")

# Always close file after opening
example.close()
