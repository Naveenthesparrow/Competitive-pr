Question Name: Can be palindrome by rotation


def is_palindrome(s):
    return s == s[::-1]

def can_be_palindrome_by_rotation(s):
    n = len(s)
    for i in range(n):
        rotated_string = s[i:] + s[:i]
        if is_palindrome(rotated_string):
            return "Yes, the rotated string is a palindrome."
    return "No, the rotated string is not a palindrome."

# Read input from the user
input_string = input("Enter the string: ").strip()

# Check if the string can be a palindrome by rotation and print the result
result = can_be_palindrome_by_rotation(input_string)
print(result)
