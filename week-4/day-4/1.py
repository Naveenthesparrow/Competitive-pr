https://leetcode.com/problems/koko-eating-bananas/description/

Question Name:  Eating Speed

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k small, h large. 
        
        def counter(k):
            count = 0
            for pile in piles:
                count += math.ceil(pile/k)
            return count
        start, end = 1, max(piles)
        while start < end:
            mid = (start+end) //2 
            temp_h = counter(mid)

            # check if h can be increased to minimize k. check lower range of k
            if temp_h <= h:
                end = mid
            
            # h is too big. Need to increase k to fit into h criteria
            else:
                start = mid +1
        
        return start