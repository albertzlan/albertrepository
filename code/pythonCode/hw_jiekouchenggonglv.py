import math


class Solution:
    @staticmethod
    def mydo(h, piles):
        print([h, piles])
        left = right = 0
        dst = list()
        res = 0
        while right < len(piles):
            # print([sum(piles[left:right + 1]) / (right - left + 1), h])
            if sum(piles[left:right + 1]) / (right - left + 1) <= h:
                if (right - left + 1) > res:
                    res = right - left + 1
                    dst.clear()
                    dst.append(str(left) + "-" + str(right))
                elif (right - left + 1) == res:
                    dst.append(str(left) + "-" + str(right))
                right += 1
            else:
                left += 1
            if left > right:
                right += 1
        # print(dst)
        if len(dst) == 0:
            return None
        return " ".join(dst)


if __name__ == "__main__":
    s = Solution()
    print(s.mydo(1, [0, 1, 2, 3, 4]))
    print(s.mydo(2, [0, 0, 100, 2, 2, 99, 0, 2]))
    print(s.mydo(3, list(range(1, 11))))
    print(s.mydo(10, list(range(10, 101, 10))))
    print(s.mydo(50, list(range(10, 101, 10))))
    print(s.mydo(100, list(range(10, 101, 10))))
    print(s.mydo(0, list([0] * 10)))
    print(s.mydo(100, list([100] * 10)))
    print(s.mydo(50, list([100] * 10)))
    print(s.mydo(0, list([100] * 10)))
