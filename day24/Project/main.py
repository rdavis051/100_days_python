
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

## some modes to know: 'r' or read, 'w' for write, 'a' for append

#with open("my_file.txt", mode="a") as file:
#    file.write("my girlfriend name is Tehera")