# File Handling in Python
# File Handling is an important aspect of programming that allows you to read from and write to files on your computer. 
# Python provides built-in functions and methods to handle files easily.
# File Handling is used to store data permanently, share data between programs, and manage large amounts of data efficiently.

# r - Read mode: Opens a file for reading only. The file pointer is placed at the beginning of the file. If the file does not exist, it raises an error.
# w - Write mode: Opens a file for writing only. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
# a - Append mode: Opens a file for appending. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.
# x - Exclusive creation mode: Creates a new file and opens it for writing. If the file already exists, it raises an error.
# b - Binary mode: Opens a file in binary mode. This is used for non-text files like images or executable files.
# t - Text mode: Opens a file in text mode. This is the default mode for text files.
# If file is not closed after operations, it can lead to memory leaks and data corruption.
# with : With keyword automatically closes the file after the block of code is executed.

# Q) Write a program to create a file and write some data into it using with statement
# Open a file in write mode
with open("example.txt", "w") as file:
# Write data to the file
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("File handling in Python is easy and fun!\n")

# Q) Take 3 input from the user and write it to a file and then retrieve the data from the file and print it
# Taking 3 inputs from the user
data = []
Miscellaneous = []
Miscellaneous.append(input("Enter Name: "))
Miscellaneous.append(input("Enter Roll No: "))
Sub_Num = int(input("Enter number of subjects: "))
for i in  range(Sub_Num):
    subject = input(f"Enter subject {i+1}: ")
    data.append(subject)

# Writing data to the file
with open("example.txt", "w") as file:
    file.write("Name: %s\n" % Miscellaneous[0])
    file.write("Roll No: %s\n" % Miscellaneous[1])
    i = 1
    for item in data:
        file.write("Subject %d: %s\n" % (i, item))
        i += 1

# Reading data from the file
with open("example.txt", "r") as file:
    content = file.readlines()
    print("\n")
    print("Data from file:")
    print("----------------")
    for line in content:
        print(line.strip())


# This is the last line