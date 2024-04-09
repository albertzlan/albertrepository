def mybfs(pos, m, n, nums, nnmax):
    visited = [[False] * n for _ in range(m)]
    # print(visited)
    tmp = list()
    tmp.append(pos)
    while len(tmp) != 0:
        ii, jj = tmp[0][0], tmp[0][1]
        # print([m, n, tmp])
        tmp.pop(0)
        # print([ii,jj,tmp)
        if visited[ii][jj] is False:
            visited[ii][jj] = True
            nums[ii][jj] = 0
            nnmax += 1
            # calculate next possible positions.
            # print([ii, jj, nums])
            if ii + 1 < m and visited[ii + 1][jj] is False and nums[ii + 1][jj] == 1:
                tmp.append([ii + 1, jj])
            if ii - 1 >= 0 and visited[ii - 1][jj] is False and nums[ii - 1][jj] == 1:
                tmp.append([ii - 1, jj])
            if jj + 1 < n and visited[ii][jj + 1] is False and nums[ii][jj + 1] == 1:
                tmp.append([ii, jj + 1])
            if jj - 1 >= 0 and visited[ii][jj - 1] is False and nums[ii][jj - 1] == 1:
                tmp.append([ii, jj - 1])
    # print(visited)
    return nnmax


class Solution:
    @staticmethod
    def jump(nums):
        m, n = nums[0]
        tmp = nums[1:]
        nmax = int(0)
        # print([m,n,tmp])
        for ii in range(m):
            for jj in range(n):
                if tmp[ii][jj] == 1:
                    # print(["bfs:", ii, jj])
                    nmax = max(mybfs([ii, jj], m, n, tmp, 0), nmax)
                    # print(tmp)
        # print(nums)
        return nmax


if __name__ == "__main__":
    s = Solution()
    print(s.jump([[2, 2], [1, 0], [1, 1]]))
    print(s.jump([[3, 3], [1, 0, 1], [0, 1, 0], [1, 0, 1]]))
    print(s.jump([[4, 4], [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]))
