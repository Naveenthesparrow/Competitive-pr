Question Name: Minimum Cost to Merge Stones

class Solution:
    def numMovesStonesII(self, s: List[int]) -> List[int]:
        s.sort()
        n = len(s)
        d1 = s[-2] - s[0] - n + 2
        d2 = s[-1] - s[1] - n + 2
        max_move = max(d1, d2)
        if d1 == 0 or d2 == 0:
            return [min(2, max_move), max_move]
        max_cnt = left = 0
        for right, x in enumerate(s):
            while s[left] <= x - n:
                left += 1
            max_cnt = max(max_cnt, right - left + 1)
        return [n - max_cnt, max_move]