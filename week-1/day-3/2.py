Question Name: Max Consecutive Ones

def longest_ones(nums, k):
    left = 0
    zero_count = 0
    max_length = 0

    for right in range(len(nums)):
        # If the current element is 0, increment the zero_count
        if nums[right] == 0:
            zero_count += 1
        
        # While the number of 0s in the window exceeds k, move the left pointer
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        # Update the maximum length of the window
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage
n = int(input().strip())
nums = list(map(int, input().strip().split()))
k = int(input().strip())

print(longest_ones(nums, k))

