def add_three_numbers(a, b, c):
    # Check if all inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        raise ValueError("They should be integers.")

    # Calculate the sum
    result = a + b + c
    return result


# Example usage
try:
    num1 = 10
    num2 = 20
    num3 = '30'  # This should raise a ValueError
    sum_result = add_three_numbers(num1, num2, num3)
    print(f"The sum of the three numbers is: {sum_result}")
except ValueError as e:
    print(e)
