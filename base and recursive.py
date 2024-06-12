def sum_natural_numbers(n):
    # Base case: if n is 1, the sum is 1
    if n == 1:
        return 1
    # Recursive case: sum of first n numbers is n + sum of first n-1 numbers
    else:
        return n + sum_natural_numbers(n - 1)

# Example usage
number = 5
result = sum_natural_numbers(number)
print(f"The sum of the first {number} natural numbers is {result}")


