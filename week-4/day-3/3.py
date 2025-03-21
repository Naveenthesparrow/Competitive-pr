https://leetcode.com/problems/find-the-shortest-superstring/description/

Question Name:  Shortest superstring


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:

        def fn(l):
            ar = [0] * ln
            for i in range(ln):
                ar[i] = {}
            return ar

        dp = [[math.inf for _ in range(len(words))] for _ in range(len(words))]
        for i in range(len(words)):
            for j in range(len(words)):
                l = len(words[j])
                for k in range(len(words[i])):
                    temp =  words[i][k:]
                    rem = len(temp)
                    if rem >= len(words[j]):continue
                    hold =  words[j][:rem]
                    if temp == hold:
                        dp[i][j] = k
                        break
                if dp[i][j] == math.inf: dp[i][j] = len(words[i]) 

        ln = len(words)
        prev = fn(ln)
        for i, j in enumerate(words):
            key = 1 << i
            prev[i][key] =  [[i], len(j)]
        
        for i in range(2, ln + 1):
            hold = fn(ln)
            for j in range(ln):
                temp = {}
                b = 1 << j
                for k in range(ln):
                    if k == j:continue
                    for x, y in prev[k].items():
                        if b & x != 0:continue
                        key = b | x
                        if key not in temp:
                            temp[key] = [[j] + y[0], y[1] + dp[j][k]]
                        else:
                            val = y[1] + dp[j][k]
                            if val < temp[key][1]:
                                temp[key] = [[j] + y[0], y[1] + dp[j][k]]
                hold[j] = temp
            prev = hold

        mn = math.inf
        ind = None
        for m in range(ln):
            for i, j in prev[m].items():
                if j[1] < mn:
                    mn = j[1]
                    ind = (m, i)
        temp = prev[ind[0]][ind[1]][0]
        ans = ''
        for i, j in enumerate(temp):
            if i == 0:
                ans += words[j]
                continue
            prev = temp[i - 1]
            lost = len(words[prev]) - dp[prev][j]
            rem = words[j][lost:]
            ans += rem
        return ans