Array = [0, 1]


def fibonacci(n):
    if n < 3:
        return n
    else:
        fib = fibonacci(n - 1)*fibonacci(n - 2) + (n-3)*fibonacci(n-3)
        Array.append(fib)
        return fib
        # return fibonacci(n - 1)*fibonacci(n - 2) + (n-3)*fibonacci(n-3)


# Driver Program

print(fibonacci(4))
print(fibonacci(9))
print(fibonacci(12))

#Time Complexity: O(n)