Question Name : Longest Chain

def find_longest_chain(pairs):
    # Sort pairs based on the second element of each pair
    pairs.sort(key=lambda x: x[1])
    
    # Initialize the current end and the longest chain length
    current_end = float('-inf')
    longest_chain = 0
    
    # Iterate through the sorted pairs
    for pair in pairs:
        if current_end < pair[0]:
            # If the current pair can be chained, update the end and increase the chain length
            current_end = pair[1]
            longest_chain += 1
            
    return longest_chain

# Example usage:
# Input handling
input_data = input().strip().split()
n = int(input_data[0])
pairs = []

for _ in range(n):
    left, right = map(int, input().strip().split())
    pairs.append([left, right])

result = find_longest_chain(pairs)
print(f"Length of the longest chain: {result}")

