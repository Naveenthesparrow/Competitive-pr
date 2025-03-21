https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/description/

Question Name:  Prefix suffix Pairs

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        MOD = 10**9+9
        mult = 31
        
        # storing frequency of previous word hashes
        hmap = collections.defaultdict(int)
        orda = ord('a')-1 # this will make char order start with 1. e.g. a=1, b=2, ...
        res = 0
        for word in words:
            # storing word hashes that are also prefixes of this word
            prefs = set()
            hhash = 0
            for ch in word:
                hhash = (hhash*mult + ord(ch)-orda) % MOD
                if hhash in hmap:
                    prefs.add(hhash)
            
            # computing hash from the end to beginning (suffix)
            hhash = 0
            m2 = 1 
            for ch in word[::-1]:
                hhash = (hhash + m2*(ord(ch)-orda)) % MOD
                if hhash in prefs:
                    res += hmap[hhash]
                m2 = (m2*mult) % MOD
            
            hmap[hhash] += 1
        
        return res