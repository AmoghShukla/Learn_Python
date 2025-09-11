# Threading in Python
# Threading is a way to run multiple threads (smaller units of a process) concurrently within a single process.
# This is useful for I/O-bound tasks, such as web scraping, file handling, or network operations, 
# where threads can run in the background while waiting for I/O operations to complete.
# Python's threading module provides a way to create and manage threads.


# Q) Write a program to print "Amogh" and "Shukla" 3 times each using threading

from threading import Thread
from time import sleep

class A(Thread):
    def run(self):
        for i in range(3):
            print("Amogh")
            sleep(2)

class B(Thread):
    def run(self):
        for i in range(3):
            print("shukla")
            sleep(2)

t1 = A()
t2 = B()

t1.start()
t2.start()


# Q) Write a program to print numbers and letters using threading

from threading import Thread
import time

def print_nums():
    for i in range(1, 6):
        print("Number :",i)
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print("Letter :",letter)
        time.sleep(1)

# Create threads
t1 = Thread(target=print_nums)
t2 = Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join() # join makes the main program wait for the thread to complete
t2.join() # join makes the main program wait for the thread to complete

print("Finished execution")