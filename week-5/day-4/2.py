https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

Question Name: sumOfPowers


class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)

        @cache
        def dp(i,prev,k,min_diff=inf):
            if k==0:
                return min_diff
            if i==n:
                return 0
            ans=dp(i+1,prev,k,min_diff)
            ans+=dp(i+1,i,k-1,min_diff if prev==None else min(min_diff,nums[i]-nums[prev]))
            return ans%int(1e9+7)
                
        
        return dp(0,None,k)