Question Name  : Generate Subsequences



def generate_subsequences(s):
    # Helper function to recursively generate subsequences
    def backtrack(start, current):
        if start == len(s):
            if current:
                subsequences.append(current)
            return
        
        # Include the current character
        backtrack(start + 1, current + s[start])
        
        # Exclude the current character
        backtrack(start + 1, current)

    subsequences = []
    backtrack(0, "")
    subsequences.sort()
    return subsequences

# Example usage:
if __name__ == "__main__":
    input_str = input("Enter a string: ").strip()
    subsequences = generate_subsequences(input_str)
    print("Output:")
    for subseq in subsequences:
        print(subseq)

# Examples:
# Input: abc
# Expected Output: a ab abc ac b bc c
#
# Input: aa
# Expected Output: a a aa

