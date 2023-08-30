cache = {}


def factorial(n):
    if n in cache:
        print("Cached: ", n)
        return cache[n]
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    cache[n] = result
    return result


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
