class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        l_dp = len(dp)
        for i in range(l_dp - 2, -1, -1):
            for j in range(i + 1, l_dp):
                print(dp, i, j)
                if dp[j] and s[i: j] in words:
                    dp[i] = True
                    break
        return dp[0]