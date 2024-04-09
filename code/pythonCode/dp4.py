import sys


def dp4(nnum, ncost, ncc, ndst):
    if nnum == 1:
        return min(ncost[0], ncost[1])
    if nnum == 0:
        return ncost[0]
    if nnum < 0:
        return 0

    print([nnum, ncc[nnum - 1]])
    if ncc[nnum - 1] > 0:
        print("1>0")
        return ncc[nnum - 1]
    if ncc[nnum - 2] > 0:
        print("2>0")
        return ncc[nnum - 2]

    print(nnum)
    t1 = dp4(nnum - 1, ncost, ncc, ndst) + ncost[nnum - 1]
    t2 = dp4(nnum - 2, ncost, ncc, ndst) + ncost[nnum - 2]
    if t1 > t2:
        ndst = dp4(nnum - 2, ncost, ncc, ndst)
        ncc[nnum - 2] = ndst
    else:
        ndst = dp4(nnum - 1, ncost, ncc, ndst) + ncost[nnum - 1]
        ncc[nnum - 1] = ndst
    return ndst


num = 10
cost = list(map(int, "1 100 1 1 1 90 1 1 80 1".split()))
cc = [0 for ii in range(num)]
dst = 0
print(dp4(num, cost, cc, dst))
