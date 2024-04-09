def mydo(pl, ii):
    if pl[ii] != ii:
        pl[ii] = mydo(pl, pl[ii])
    return pl[ii]


class Solution:
    @staticmethod
    def mymethod(n, m, cost):
        if m == 1:
            return -1
        edges = set()
        parlist = [ii for ii in range(n + 1)]
        cost.sort(key=lambda x: x[2])
        for cur, nxt, ww, link in cost:
            if link == 1:
                parlist[cur] = nxt
                edges.add((cur, nxt))
        res = 0
        for cur, nxt, ww, link in cost:
            a = mydo(parlist, cur)
            b = mydo(parlist, nxt)
            if a != b:
                parlist[a] = b
                res += ww
                edges.add((cur, nxt))
        print(edges)
        if res == 0:
            return -1
        return res

    @staticmethod
    def domethod(n, m, cost):
        if m == 1:
            return -1
        edges = set()
        parlist = [ii for ii in range(n + 1)]
        cost.sort(key=lambda x: x[2])
        for cur, nxt, ww, link in cost:
            if link == 1:
                parlist[cur] = nxt
                edges.add((cur, nxt))
        res = 0
        for cur, nxt, ww, link in cost:
            a = mydo(parlist, cur)
            b = mydo(parlist, nxt)
            if a != b:
                parlist[a] = b
                res += ww
                edges.add((cur, nxt))
        print(edges)
        if res == 0:
            return -1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.domethod(3, 3, [[1, 2, 3, 0], [1, 3, 1, 0], [2, 3, 5, 0]]))
    print(s.domethod(3, 1, [[1, 2, 5, 0]]))
    print(s.domethod(3, 3, [[1, 2, 3, 0], [1, 3, 1, 0], [2, 3, 5, 1]]))
