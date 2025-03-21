Question Name:  Russian Doll Envelopes

from bisect import bisect_left

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    heights = [e[1] for e in envelopes]
    dp = []
    
    for h in heights:
        i = bisect_left(dp, h)
        if i < len(dp):
            dp[i] = h
        else:
            dp.append(h)
    
    return len(dp)

# Example usage:
envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(maxEnvelopes(envelopes))  # Output: 3
