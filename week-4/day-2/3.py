https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

Question Name:  Convert string

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        G = defaultdict(list)
        for i in range(len(cost)):
            G[original[i]].append((changed[i],cost[i]))
        
        @cache
        def getShortest(i,j):
            if i == j:
                return 0
            Q = [(0,i)]
            D = {}
            D[i] = 0
            while Q:
                d,node = heappop(Q)
                if node == j: return d
                for node1, c in G[node]:
                    if node1 not in D or D[node1] > c + d:
                        D[node1] = c + d
                        heappush(Q,(d+c,node1))
            return inf

        m = len(source)
        Trie = lambda : defaultdict(Trie)
        trie = Trie()
        
        for w in list(set(original) | set(changed)):
            curr = trie
            for ch in w:
                curr = curr[ch]
            curr['#'] = w
        
        def search(i,currS,currT):
            ans = []
            if '#' in currS and '#' in currT:
                ans.append((currS['#'],currT['#']))
            if (i == m) or (source[i] not in currS) or (target[i] not in currT):
                return ans
            ans.extend(search(i+1,currS[source[i]],currT[target[i]]))
            return ans
            
        @cache
        def dp(i):
            if i == m:
                return 0
            IDX = search(i,trie,trie)
            if not IDX:
                return inf if source[i] != target[i] else dp(i+1)
            ans = inf if source[i] != target[i] else dp(i+1)
            return min(ans, min(getShortest(x,y) + dp(i+len(x)) for x,y in IDX))
 
        ans = dp(0)
        return ans if ans < inf else -1