https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/

Question Name: Beautiful Indices

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def get_indexes(a, p=19, r=1_000_000_007):
            length = len(a)
            p_ = pow(p, length, r)
            current = 0

            target = 0
            for elem in a:
                target *= p
                target += (ord(elem) - 96) * p
                target %= r

            indexes = []
            for j, right in enumerate(s):
                if j >= length:
                    left = s[j - length]
                    current -= (ord(left) - 96) * p_

                current *= p
                current += (ord(right) - 96) * p
                current %= r

                # do not check equality, because r is big enough
                if current == target:
                    indexes.append(j - length + 1)
            return indexes
        
        indexes_1 = get_indexes(a)
        indexes_2 = get_indexes(b)

        result = []
        x = y = 0
        while x < len(indexes_1) and y < len(indexes_2):
            i = indexes_1[x]
            j = indexes_2[y]
            if abs(j - i) <= k:
                result.append(i)
                x += 1
            elif i < j:
                x += 1
            else:
                y += 1
        return result