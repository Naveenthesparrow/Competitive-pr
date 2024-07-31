Question Name: Longest Increasing Subsequence


def length_of_lis(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # Initialize DP array with 1

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Example usage
n = int(input().strip())
nums = list(map(int, input().strip().split()))
print(length_of_lis(nums))
