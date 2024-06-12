def find_second_smallest(numbers):
    if len(numbers) < 2:
        return None  # Return None if there are less than 2 elements in the list

    # Initialize the first and second smallest numbers to infinity
    first = second = float('inf')

    for number in numbers:
        # Update first and second accordingly
        if number < first:
            second = first
            first = number
        elif first < number < second:
            second = number

    return second


# Given list
numbers = [3, 45, 12, 9, 65]

# Find the second smallest number
second_smallest = find_second_smallest(numbers)

# Print the second smallest number
if second_smallest is not None:
    print(f"The second smallest number is: {second_smallest}")
else:
    print("The list does not have enough elements to find the second smallest number.")
