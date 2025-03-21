Question Name: Maximum Length of Pair Chain


def findLongestChain(pairs):
    pairs.sort(key=lambda x: x[1])
    current_end = float('-inf')
    longest_chain = 0
    
    for pair in pairs:
        if current_end < pair[0]:
            current_end = pair[1]
            longest_chain += 1
    
    return longest_chain

# Example usage:
pairs = [[1, 2], [2, 3], [3, 4]]
print(findLongestChain(pairs))  # Output: 2
