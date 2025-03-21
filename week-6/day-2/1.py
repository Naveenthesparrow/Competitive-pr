https://leetcode.com/problems/the-number-of-good-subsets/

Question Name:  Number-of-good-subsets

class Solution:
    def __init__(self):
        self.goodnum = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]
        self.sgoodnum = set(self.goodnum)
        self.goodset = set([])
        @cache
        def dfs(i,mask):
            self.goodset.add(mask)
            if i == len(self.goodnum):
                return 
            dfs(i+1,mask)
            possible = True
            for j in range(i):
                if mask & (1<<j):
                    if gcd(self.goodnum[i],self.goodnum[j]) > 1:
                        possible = False
                        break
            if possible:
                dfs(i+1,mask | (1<<i))
        dfs(0,0)
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        ones = nums.count(1)
        res0 = pow(2,ones,10**9+7) - 1
        res1 = 0
        nums = [n for n in nums if n in self.goodnum]
        freq = Counter(nums)
        for mask in self.goodset:
            curr = 0
            for i in range(18):
                if not mask & (1 << i):
                    continue
                if self.goodnum[i] not in freq:
                    curr = 0
                    break
                else:
                    if curr:
                        curr *= freq[self.goodnum[i]] % (10**9+7)
                    else:
                        curr = freq[self.goodnum[i]] % (10**9+7)
            res1 += curr
        if not res1:
            return 0
        if not res0:
            return res1 % (10**9+7)
        return (res0+1)*res1 % (10**9+7)