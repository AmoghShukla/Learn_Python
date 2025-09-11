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

f = open("somanysample.txt", "x")  # Open a file in exclusive creation mode
f.write("Hello, World!\n")    # Write to the file
f.close()                      # Close the file
