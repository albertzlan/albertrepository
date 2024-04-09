class Solution:
    @staticmethod
    def mydo(nn, weig):
        if sum(weig) % 2 != 0:  # 重量和为奇数，肯定不能重量均分
            return -1
        dst = int(sum(weig) / 2)
        print(["dst:", dst])
        dp = [4 for _ in range(dst + 1)]
        dp[0] = 0  # 引导正好装满的重要因子
        for ii in range(nn):
            for ww in range(dst, weig[ii] - 1, -1):
                dp[ww] = min(dp[ww], dp[ww - weig[ii]] + 1)
                # print([ii,ww,dp])
        print(dp)
        if dp[-1] == 4:
            return -1
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.mydo(4, [3, 3, 6, 4]))
    print(s.mydo(10, [1, 1, 1, 1, 1, 9, 8, 3, 7, 10]))
    print(s.mydo(11, [1, 1, 1, 1, 1, 1, 9, 8, 3, 7, 10]))
