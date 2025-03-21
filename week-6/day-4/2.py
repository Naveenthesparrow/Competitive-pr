https://leetcode.com/problems/build-array-from-permutation/description/

Question Name: buildArray

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        list_1 = []
        for i in range(0,len(nums)):
            list_1.append(nums[nums[i]])
        return list_1
            

