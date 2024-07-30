Question Name  : Subset Sum


def can_partition(nums):
    total_sum = sum(nums)
    
    # If the total sum is odd, it's impossible to partition into two subsets with equal sum
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(nums)
    
    # Initialize DP table
    dp = [False] * (target + 1)
    dp[0] = True  # There's always a subset with sum 0 (the empty subset)
    
    for num in nums:
        # Update the DP table in reverse to avoid overwriting results of the same iteration
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    nums = list(map(int, input("Enter the elements separated by space: ").split()))
    result = can_partition(nums)
    print("true" if result else "false")
