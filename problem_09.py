# Problem 9: Find average of numbers in a list
# Find and fix the error

numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(f"Average: {average}")
