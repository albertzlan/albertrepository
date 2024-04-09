class Solution:
    def jump(self, nums):
        """
        dp[0][n-1]=min(ii=1...nums[0]:dp[ii][n-1])
        """
        if len(nums) == 1:
            return 0
        if nums[0] == 0:  # 如果跳到0的位置，则会一直跳不出去，故需要返回一个无穷大。
            return 10001
        if nums[0] >= (len(nums) - 1):
            return 1
        else:
            mmin = 1001
            for ii in range(1, nums[0] + 1):
                tmp = self.jump(nums[ii:])
                # print("ii:"+str(ii))
                # print("tmp:"+str(tmp))
                if tmp < mmin:
                    mmin = tmp
                    # print("mmin:"+str(mmin))
            steps = mmin + 1
        return steps


if __name__ == "__main__":
    ins = [5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0,
           3, 8, 5]
    s = Solution()
    print(s.jump(ins))
