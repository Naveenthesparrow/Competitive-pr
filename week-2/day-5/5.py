Question Name: Longest Increasing Subsequence

from bisect import bisect_left

def lengthOfLIS(nums):
    dp = []
    for num in nums:
        i = bisect_left(dp, num)
        if i < len(dp):
            dp[i] = num
        else:
            dp.append(num)
    return len(dp)

# Example usage:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))  # Output: 4
