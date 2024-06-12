# Read numbers from the file
with open('XYZ1.txt', 'r') as file:
    numbers = [int(num) for num in file.readlines()]

# Find the maximum number
max_num = max(numbers)

# Calculate the sum of all numbers
total_sum = sum(numbers)

# Print the results
print("Maximum number in the list:", max_num)
print("Sum of all numbers in the list:", total_sum)
