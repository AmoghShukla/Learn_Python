with open("xyz.txt", "r") as f1, open("copy.txt", "w") as f2:
    for line in f1:
        f2.write(line)
    
# with open("xyz.txt", "w") as f:
#     f.write("This is a new line.\n")
#     f.write("This will overwrite the existing content.\n")

