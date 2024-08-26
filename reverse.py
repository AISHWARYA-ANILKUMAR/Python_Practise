# Using reversed() with a string
str = "hello"
reversed_str = reversed(str)

# Convert the reversed iterator to a list
reversed_list = list(reversed_str)

print(reversed_list)  # Output: ['o', 'l', 'l', 'e', 'h']

# Alternatively, join the reversed it    erator into a single string
reversed_string = ''.join(reversed(str))

print(reversed_string)  # Output: 'olleh'
