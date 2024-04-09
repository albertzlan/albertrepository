import sys


def hj32(src):  # 运行时间：2001ms 占用内存：4664KB 使用语言：Python 3 用例通过率：91.30%
    if len(src) == 1:
        return 1
    dstlen = 0
    for sindex in range(0, len(src), 1):
        temp = src[sindex:]
        # print(temp)
        for ii in range(len(temp), dstlen, -1):
            tps = temp[:ii]
            if tps == tps[::-1]:
                if dstlen < len(tps):
                    dstlen = len(tps)
                    print(str(sindex) + "vs" + str(sindex + ii) + ": " + tps)
                    break
    return dstlen


def hj32_2(src):  # RecursionError: maximum recursion depth exceeded while calling a Python object
    if len(src) == 1:
        return 1
    llen = hj32(src[1:])
    clen = 0
    for ii in range(len(src), 1, -1):
        # print(ii)
        temp = src[:ii]
        if temp == temp[::-1]:
            if clen < len(temp):
                clen = len(temp)
                print(temp + "==" + temp[::-1])
                break
        # else:
        #     print(temp+"!="+temp[::-1])
    return max(llen, clen)


if __name__ == "__main__":
    # print((line[:-1]))
    sstr = ('cvhuocqtmstfisgzwhutwoscfomfocfktliktumejbfkugpmhlck'
            'ljrjbczojzoxwpskkxfbkignmlnejujxwwpsiovuvkflhjdqjtvd'
            'dloqxdjsvntygvsyqvmwioqgtuqmlpdnvxmjkenrltmenvhcqdrp'
            'twerthumwezrcidrzehwyskmovsjkhkitpbemujveknxhscjokkd'
            'ivssoodxswcoqebouckkhyiwrbydyh')
    print(hj32(sstr))
