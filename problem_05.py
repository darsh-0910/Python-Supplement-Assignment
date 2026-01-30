# Problem 5: Count vowels in a string
# Find and fix the error

text = "Hello World"
vowels = "aeiou"
count = 0
for char in text.lower():
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")
