Question Name:  Maximum Subarray Sum with One Deletion

def maxSumWithOneDeletion(arr):
    n = len(arr)
    forward = [0] * n
    backward = [0] * n
    
    max_sum = arr[0]
    forward[0] = arr[0]
    
    for i in range(1, n):
        forward[i] = max(arr[i], forward[i-1] + arr[i])
        max_sum = max(max_sum, forward[i])
    
    backward[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        backward[i] = max(arr[i], backward[i+1] + arr[i])
    
    for i in range(1, n-1):
        max_sum = max(max_sum, forward[i-1] + backward[i+1])
    
    return max_sum

# Example usage:
arr = [1, -2, 0, 3]
print(maxSumWithOneDeletion(arr))  # Output: 4
