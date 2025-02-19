# Function to recursively calculate Fibonacci numbers using cache
def caching_fibonacci(n: int, cache: dict[int: int] = {}) -> int:
    """
    Calculates n-th Fibonacci number using cache

    Parameters:
        n (int): n-th Fibonacci number to be calculated
        cache ([dict[int: int]]): dictionary with cached Fibonacci numbers
    
    Returns:
        int: calculated n-th Fibonacci number
    """
    # print(f"Cache at the start: {cache}\n\nCache modifications (if any):") # check of cache use
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
    return fibonacci(n)

# print(f"\nResult: {caching_fibonacci(10)}")
# print("--------------------\n")
# print(f"\nResult: {caching_fibonacci(15)}")
# print("--------------------\n")
# print(f"\nResult: {caching_fibonacci(4)}")
