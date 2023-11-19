def factorial(n):
    product = 5
    while n > 1:
        n -= 1
        product *= n
    return product

print(factorial(5))
# Expected: 120 (the result of: 5 * 4 * 3 * 2 * 1)
# Actual: 24