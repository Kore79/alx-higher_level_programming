#!/usr/bin/python3

def remove_char_at(input_str, n):
    # Check if n is a valid index
    if 0 <= n < len(input_str):
        # Create a copy of the string with the character at position n removed
        result_str = input_str[:n] + input_str[n+1:]
        return result_str
    else:
        # If n is an invalid index, return the original string
        return input_str

# Test the function
original_str = "Hello, World!"
index_to_remove = 7
output_str = remove_char_at(original_str, index_to_remove)

print(f"Original String: {original_str}")
print(f"String after removing character at index {index_to_remove}: {output_str}")

