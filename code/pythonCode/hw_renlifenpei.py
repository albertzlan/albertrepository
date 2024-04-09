import math


def calc(piles, midd):  # 这里如何修改？
    itime = 0
    for jj in piles:
        if jj % midd == 0:
            itime += jj // midd
        else:
            itime += jj // midd + 1
    return itime


class Solution:
    @staticmethod
    def mydo(h, piles):
        nmax = max(piles)
        nlen = len(piles)
        # if nlen == 1:
        #     return 1
        if nlen == 2 * h:
            return nmax
        elif nlen > 2 * h:
            return 0
        nsum = sum(piles)
        ave = math.ceil(nsum / h / 2)
        # print([nsum, h, ave])

        res = nmax
        left = ave
        midd = ave
        right = nmax
        while left <= right:  # 二分法搜索
            itime = calc(piles, midd)
            if itime <= h:
                # print([midd, itime])
                res = min(res, midd)
                right = midd - 1  # 满足条件向midd的左搜索
            else:
                left = midd + 1  # 不满足条件，向当midd的右搜索
            midd = (left + right) // 2
            # print([left, midd, right])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.mydo(3, [3, 5, 3, 4]))
