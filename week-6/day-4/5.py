https://leetcode.com/problems/permutation-difference-between-two-strings/description/

Question Name: findPermutationDifference


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ht: dict[str, int] = dict()
        for i in range(len(s)):
            if s[i] in ht:
                ht[s[i]] = abs(ht[s[i]] - i)
            else:
                ht[s[i]] = i
            if t[i] in ht:
                ht[t[i]] = abs(ht[t[i]] - i)
            else:
                ht[t[i]] = i
        return sum(ht.values())