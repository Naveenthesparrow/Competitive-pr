https://leetcode.com/problems/percentage-of-letter-in-string/description/

Question Name: percentageLetter

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        l=len(s)
        count=0
        for i in s:
            if i==letter:
                count+=1
            else:
                pass
        return int((count/l)*100)        