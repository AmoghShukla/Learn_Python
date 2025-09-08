def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for f in fib():
    if f > 100:
        break
    print(f)

# Here, Generators.py defines a generator function `fib()` that yields Fibonacci numbers indefinitely. 
# The for loop iterates over the generated Fibonacci numbers and prints them until a number greater than 100 is encountered, at which point the loop breaks.