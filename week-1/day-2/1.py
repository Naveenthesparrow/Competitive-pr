Question Name: Eating Speed

def can_finish(piles, k, h):
    hours = 0
    for pile in piles:
        hours += (pile + k - 1) // k  # Equivalent to math.ceil(pile / k)
    return hours <= h

def min_eating_speed(piles, h):
    left, right = 1, max(piles)
    
    while left < right:
        mid = (left + right) // 2
        if can_finish(piles, mid, h):
            right = mid  # Try a smaller eating speed
        else:
            left = mid + 1  # Increase the eating speed
    
    return left

if __name__ == "__main__":
    n = int(input("Enter the number of piles: "))
    piles = list(map(int, input("Enter the piles separated by space: ").split()))
    h = int(input("Enter the number of hours: "))
    result = min_eating_speed(piles, h)
    print(result)
