Question Name: Anagrams



def are_anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return "Anagrams"
    else:
        return "Not Anagrams"

# Taking input from the user in a single line
input_line = input("Enter the two strings separated by a space: ").strip()

# Splitting the input into two strings
str1, str2 = input_line.split()

# Check if the given strings are anagrams and print the result
print(are_anagrams(str1, str2))
