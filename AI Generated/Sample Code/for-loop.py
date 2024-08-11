# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Variable to store the sum of even numbers
sum_of_evens = 0

# Iterate over each number in the list
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        # Add the even number to the sum
        sum_of_evens += number

# Print the result
print("The sum of even numbers is:", sum_of_evens)
