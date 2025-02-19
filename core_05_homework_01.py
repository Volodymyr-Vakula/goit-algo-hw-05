from typing import Callable

# Function to recursively calculate Fibonacci numbers using cache
def caching_fibonacci() -> Callable[[int], int]:
    """
    Calculates Fibonacci numbers using cache

    Returns:
        Callable ([int], int): function to recursively calculate n-th Fibonacci number
    """
    cache = {}
    # print(f"Cache at the start: {cache}\n\nCache modifications (if any):") # check of cache use
    # Function to recursively calculate n-th Fibonacci number
    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 0:
            cache[0] = 0
            # print(cache) # check of cache use
            return 0
        if n == 1:
            cache[1] = 1
            # print(cache) # check of cache use
            return 1
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        # print(cache) # check of cache use
        return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(f"\nResult: {fib(10)}")
print("--------------------\n")
print(f"\nResult: {fib(15)}")
