import math


class Solution:
    @staticmethod
    def mydo(h):
        dp = [1] * (h + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        cut = [[1] for _ in range(h + 1)]
        cut[0] = [0]
        cut[1] = [1]
        cut[2] = [2]
        cut[3] = [3]
        cut[4] = [4]
        for ii in range(5, h + 1, 1):
            a = ii // 2
            b = ii - a
            dp[ii] = dp[a] * dp[b]
            cut[ii] = cut[a] + cut[b]
            # print([ii, a, b, dp[ii], cut[ii]])
        print(dp)
        cut[h].sort()
        print(cut[h])
        while cut[h].count(2) > 1:
            cut[h] = cut[h][2:] + [4]
            cut[h].sort()
        return cut[h]


if __name__ == "__main__":
    s = Solution()
    print(s.mydo(50))


