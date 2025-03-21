https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

Question Name:Balanced string split


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = []
        sub = ''
        count1 = 0
        count2 = 0
        i = 0
        while len(s) > i:
            while len(s) > i and s[i] == 'R':
                sub += s[i]
                count1 += 1
                i += 1
                if count1 == count2:
                    l.append(sub)
                    sub = ''
                    count2 = 0
                    count1 = 0
            while len(s) > i and s[i] == 'L':
                sub += s[i]
                count2 += 1
                i += 1
                if count1 == count2:
                    l.append(sub)
                    sub = ''
                    count2 = 0
                    count1 = 0
        return len(l)