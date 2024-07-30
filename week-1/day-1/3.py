Question Name  : Generate Parentheses   

def generate_parentheses(n):
    def backtrack(s, open_count, close_count):
        if len(s) == 2 * n:
            result.append(s)
            return
        
        if open_count < n:
            backtrack(s + '(', open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(s + ')', open_count, close_count + 1)

    result = []
    backtrack('', 0, 0)
    result.sort()  # Ensure the results are in lexicographically increasing order
    return result

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter the number of pairs of parentheses: ").strip())
    combinations = generate_parentheses(n)
    print("Output:")
    for combo in combinations:
        print(combo ,end=” “)

# Examples
# Input: 3
# Expected Output: ((())) (()()) (())() ()(()) ()()()
#
# Input: 1
# Expected Output: ()

