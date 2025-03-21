https://leetcode.com/problems/valid-perfect-square/description/

Question Name: isPerfectSquare

 class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        q = num // 4  # Integer division in Python
        i = 1
        while i * i <= num:  # Check if i*i exceeds num
            if i * i == num:
                return True
            i += 1
        return False