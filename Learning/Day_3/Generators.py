# Generators in Python
# Generators are a special type of iterable, like lists or tuples.
# However, unlike lists, they do not store their contents in memory.
# Instead, they generate values on the fly and yield them one at a time, which makes them more memory efficient for large datasets.
# Generators are defined using functions and the yield statement.

def simple_generator(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            yield i

n = int(input("Enter a number to generate odd numbers up to that number: "))
gen = simple_generator(n)

m = int(input("How Many Numbers you need? : "))
for i in range(m):
    print(next(gen))

# Q1) Create a generator that yields the squares of numbers from 1 to n.
def square_generator(n):
    for i in range(1, n+1):
        yield i * i
n = int(input("Enter a number to generate squares up to that number: "))
gen = square_generator(n)

m = int(input("How Many Numbers you need? : "))
for i in range(m):
    print(next(gen))

# Q2) Create a generator that yields the Fibonacci sequence up to n terms.

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
n = int(input("Enter the number of terms for Fibonacci sequence: "))
gen = fib(n)
m = int(input("How Many Numbers you need? : "))
for i in range(m):
    print(next(gen))


# Q3) Create a generator that yields prime numbers up to n.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_generator(n):
    for i in range(2, n + 1):
        if is_prime(i):
            yield i
n = int(input("Enter a number to generate prime numbers up to that number: "))
gen = prime_generator(n)

m = int(input("How Many Numbers you need? : "))
for i in range(m):
    print(next(gen))