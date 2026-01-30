# Problem 11: Count occurrences of each character
# Find and fix the error

text = "programming"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char,0) + 1
print(char_count)
