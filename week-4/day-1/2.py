https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/


Question Name: Unique Characters

class Solution:
    def maxLength(self, a: List[str]) -> int:
        def f(i, s):
            if i == len(a):
                return len(s)

            result = f(i+1, s)
            g = s | {*a[i]}
            if len(g) == len(s) + len(a[i]):
                result = max(result, f(i+1, g))

            return result
        
        return f(0, set())