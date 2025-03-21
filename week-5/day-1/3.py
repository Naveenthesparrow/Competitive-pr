https://leetcode.com/problems/palindrome-number/

Question Name: isPalindrome

 def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        lis = []
        while x >= 10:
            lis.append(x % 10)
            x //= 10
        lis.append(x)
        for i in range(int(math.ceil(len(lis)/2))):
            if lis[i] != lis[len(lis)-i-1]:
                return False
        return True