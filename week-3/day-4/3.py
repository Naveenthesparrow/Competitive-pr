Question Name: canPartition


def canPartition(nums):
    total_sum = sum(nums)
    
    # If the total sum is odd, it's not possible to partition it into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(nums)
    
    # DP array to check for possible subset sums
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]

# Input
n = int(input())
nums = list(map(int, input().split()))

# Output
print("true" if canPartition(nums) else "false")
