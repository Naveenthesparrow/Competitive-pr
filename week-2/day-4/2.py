Question Name:  Distinct Subsequences II

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp=defaultdict(int)
        a=0
        b=10**9 + 7
        for c in s:
            tmp=a-dp[c]
            dp[c]=(a + 1) % b
            a=(tmp + dp[c])%b
        return a