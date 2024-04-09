class Solution:
    @staticmethod
    def bfs(pos, m, n, nums, flag):
        visited = [[False] * n for _ in range(m)]
        # print(visited)
        tmp = list()
        tmp.append(pos)
        while len(tmp) != 0:
            ii, jj = tmp[0][0], tmp[0][1]
            # print([m, n, tmp])
            tmp.pop(0)
            if visited[ii][jj] is False:
                visited[ii][jj] = True
                if nums[ii][jj] == flag:
                    nums[ii][jj] += 1
                # calculate next possible positions.
                # print([ii,jj,tmp])
                if ii + 1 < m and visited[ii + 1][jj] is False and nums[ii + 1][jj] != 1:
                    tmp.append([ii + 1, jj])
                if ii - 1 >= 0 and visited[ii - 1][jj] is False and nums[ii - 1][jj] != 1:
                    tmp.append([ii - 1, jj])
                if jj + 1 < n and visited[ii][jj + 1] is False and nums[ii][jj + 1] != 1:
                    tmp.append([ii, jj + 1])
                if jj - 1 >= 0 and visited[ii][jj - 1] is False and nums[ii][jj - 1] != 1:
                    tmp.append([ii, jj - 1])
        # print(visited)

    def jump(self, m, n, nums):
        pos = []
        for ii in range(m):
            for jj in range(n):
                if nums[ii][jj] == 2:
                    pos.append([ii, jj])
        # print(pos)
        self.bfs(pos[0], m, n, nums, 3)
        # print(nums)
        self.bfs(pos[1], m, n, nums, 4)
        # print(nums)
        nn = 0
        for ii in range(m):
            for jj in range(n):
                if nums[ii][jj] == 5:
                    nn += 1
        return nn


if __name__ == "__main__":
    s = Solution()
    print(s.jump(4, 4, [[2, 1, 0, 3], [0, 1, 2, 1], [0, 3, 0, 0], [0, 0, 0, 0]]))
    print(s.jump(4, 4, [[2, 1, 2, 3], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]))
    print(s.jump(3, 3, [[2, 1, 0], [0, 1, 3, ], [0, 0, 2]]))
    print(s.jump(3, 3, [[2, 0, 0], [1, 1, 0, ], [0, 0, 2]]))
    print(s.jump(5, 5, [[2, 1, 0, 0, 3], [0, 1, 2, 1, 0], [0, 3, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
    # print(s.jump(3, 3, [[2, 1, 0], [0, 1, 3], [0, 0, 2]]))
