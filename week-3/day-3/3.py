Question Name: pushDominoes


def pushDominoes(dominoes):
    n = len(dominoes)
    dist = [float('inf')] * n

    # First pass: from left to right
    for i in range(n):
        if dominoes[i] == 'R':
            dist[i] = 0
        elif i > 0 and dist[i - 1] != float('inf'):
            dist[i] = dist[i - 1] + 1

    # Second pass: from right to left
    for i in range(n - 1, -1, -1):
        if dominoes[i] == 'L':
            dist[i] = 0
        elif i < n - 1 and dist[i + 1] != float('inf'):
            dist[i] = min(dist[i], dist[i + 1] + 1)
    
    # Determine final state
    result = []
    for i in range(n):
        if dominoes[i] == '.':
            left_dist = dist[i] if i > 0 else float('inf')
            right_dist = dist[i] if i < n - 1 else float('inf')
            if left_dist < right_dist:
                result.append('R')
            elif right_dist < left_dist:
                result.append('L')
            else:
                result.append('.')
        else:
            result.append(dominoes[i])
    
    return ''.join(result)

# Example usage:
dominoes = input()  # Read the input string
print(pushDominoes(dominoes))
