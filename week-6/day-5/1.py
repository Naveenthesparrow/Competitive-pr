https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

Question Name:  findAnagrams

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        pmap = [0] * 26
        smap = [0] * 26
        result = []

        for char in p:
            pmap[ord(char) - ord('a')] += 1

        for i in range(len(p)):
            smap[ord(s[i]) - ord('a')] += 1

        if smap == pmap:
            result.append(0)

        for i in range(len(p), len(s)):
            smap[ord(s[i]) - ord('a')] += 1
            smap[ord(s[i - len(p)]) - ord('a')] -= 1

            if smap == pmap:
                result.append(i - len(p) + 1)

        return result