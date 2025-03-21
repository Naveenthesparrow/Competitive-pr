https://leetcode.com/problems/counting-words-with-a-given-prefix/description/

Question Name: prefixCount

class Solution(object):
    def prefixCount(self, words, pref):
        ans = 0
        for s in words:
            if s.startswith(pref):
                ans += 1
        return ans