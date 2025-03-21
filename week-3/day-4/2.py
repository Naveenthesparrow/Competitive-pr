Question Name: minEatingSpeed

import math

def minEatingSpeed(piles, h):
    # Function to determine if Koko can eat all bananas at a speed of k
    def canFinish(k):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours <= h

    # Binary search to find the minimum k
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if canFinish(mid):
            right = mid  # Try to find a smaller k
        else:
            left = mid + 1  # Increase k since mid is too small
    
    return left

# Input
n = int(input())  # Number of piles
piles = list(map(int, input().split()))  # Piles of bananas
h = int(input())  # Number of hours

# Output
print(minEatingSpeed(piles, h))
