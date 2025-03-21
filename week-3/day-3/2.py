Question Name: min_max_moves


def min_max_moves(stones):
    stones.sort()
    n = len(stones)
    
    # Finding minimum number of moves
    min_moves = float('inf')
    left = 0
    
    for right in range(n):
        while stones[right] - stones[left] > n - 3:
            left += 1
        min_moves = min(min_moves, n - (right - left + 1))
    
    # Finding maximum number of moves
    max_moves = 0
    # The maximum moves are determined by the maximum gap between stones minus 1
    for i in range(1, n):
        max_moves = max(max_moves, stones[i] - stones[i - 1] - 1)
    
    return min_moves, max_moves

# Input from the user
n = int(input("Enter the number of stones: "))
stones = list(map(int, input("Enter the positions of the stones separated by spaces: ").split()))

min_moves, max_moves = min_max_moves(stones)
print(f"{min_moves} {max_moves}")
