https://leetcode.com/problems/maximum-length-of-pair-chain/description/

Question Name:  Length Pair

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        last = pairs[0]
        cnt = 1

        for i in range(1, len(pairs)):
            if last[-1] < pairs[i][0]:
                last = pairs[i]
                cnt +=1
            elif last[-1] > pairs[i][-1]:
                last = pairs[i]            

        return cnt