https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

Question Name: sumOfPower


class Solution(object):
    def power(self, cnt):
        mod = 1000000007
        val = 1
        for j in range(self.n - cnt):
            val = (val * 2) % mod
        return val

    def solve(self, i, k, cnt, nums):
        mod = 1000000007
        if k < 0:
            return 0
        if k == 0:
            val = self.power(cnt)
            return val
        if i == self.n:
            return 0
        ans = self.solve(i + 1, k - nums[i], cnt + 1, nums)
        ans = (ans + self.solve(i + 1, k, cnt, nums)) % mod
        return ans

    def sumOfPower(self, nums, k):
        self.n = len(nums)
        return self.solve(0, k, 0, nums)