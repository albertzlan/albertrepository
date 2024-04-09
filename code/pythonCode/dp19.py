import sys


def dp19(ml, nl, cc):  # 动态规划
    # iidst = 0
    icnt = 0
    if len(ml) == 0 or len(nl) == 0:
        return 0
    # for ii in range(len(m))
    if ml[0] == nl[0]:
        # print(["ml[0] == nl[0]",ml[0],nl[0]])
        if cc[len(ml)][len(nl)] > 0:
            icnt += 1
            iidst = cc[len(ml)][len(nl)]
        else:
            iidst = dp19(ml[1:], nl[1:], cc) + 1
    else:
        if cc[len(ml) - 1][len(nl)] > 0 and cc[len(ml)][len(nl) - 1] > 0:
            # print(">>")
            icnt += 1
            iidst = max(cc[len(ml) - 1][len(nl)], cc[len(ml)][len(nl) - 1])
        elif cc[len(ml) - 1][len(nl)] > 0 and cc[len(ml)][len(nl) - 1] == 0:
            # print(">=")
            icnt += 1
            iidst = max(cc[len(ml) - 1][len(nl)], dp19(ml[:], nl[1:], cc))
        elif cc[len(ml) - 1][len(nl)] == 0 and cc[len(ml)][len(nl) - 1] > 0:
            # print("=>")
            icnt += 1
            iidst = max(dp19(ml[1:], nl[:], cc), cc[len(ml)][len(nl) - 1])
        else:
            # print(["NO...",ml,nl,cc[len(ml) - 1][len(nl)],cc[len(ml)][len(nl) - 1]])
            iidst = max(dp19(ml[:], nl[1:], cc), dp19(ml[1:], nl[:], cc))
    cc[len(ml)][len(nl)] = iidst
    # print([cc,iidst])
    # if icnt>2:
    #     print(icnt)
    return iidst


"""
# 您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# 4/16 组用例通过；运行时间 2001ms;占用内存 6552KB
50 50
nwlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarc
bynecdyggxxpklorellnmpapqfwkhopkmcoqhnwnkuewhsqmgb
answer:14
#您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
#7/16 组用例通过;运行时间 2001ms;占用内存 15524KB
100 100
nwlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmcoqhnwnkuewhsqmgb
buqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcacehchzvfrkmlnozjkpqpxrjxkitzyx
answer:27
"""

[m, n] = [100, 100]
mli = "nwlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmcoqhnwnkuewhsqmgb"
nli = "buqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcacehchzvfrkmlnozjkpqpxrjxkitzyx"
ccli = [[0 for ii in range(int(n) + 1)] for jj in range(int(m) + 1)]
print(dp19(mli, nli, ccli))
# print(cc)
