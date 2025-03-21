Question Name : [Maximum Score]

def max_score(tokens, power):
    tokens.sort()
    i, j = 0, len(tokens) - 1
    score, max_score = 0, 0
    
    while i <= j:
        if power >= tokens[i]:
            power -= tokens[i]
            score += 1
            i += 1
            max_score = max(max_score, score)
        elif score > 0:
            power += tokens[j]
            score -= 1
            j -= 1
        else:
            break
    
    return max_score

# Example usage:
# Input handling
n = int(input().strip())
tokens = list(map(int, input().strip().split()))
power = int(input().strip())

result = max_score(tokens, power)
print(result)
