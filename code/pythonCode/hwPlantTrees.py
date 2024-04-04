class solution:
    @staticmethod
    def hwTest(testIn):
        srcIn = testIn
        repL = []
        for i in srcIn:
            cnt = srcIn.count(i)
            if (cnt == 1) and (i not in repL):
                repLf = srcIn.find(i)  # the first index
                repLl = srcIn.rfind(i)  # the last index
                # keep this sequence...
                repL.append(repLf)
                repL.append(repLl)
                repL.append(i)
        if len(repL) == 0:
            return 1
        else:
            print(repL)
            times = int(len(repL) * 3)
            firstI = 0
            lastI = 0
            maxLen = []
            for i in range(times):
                # firstI = repL[3:i]
                # lastI = repL[3:i + 1]
                counter = 0
                temp1 = srcIn[firstI:lastI]  # 重复字符之间的字符
                for ltr in temp1:
                    counter += 1
                    temp2 = srcIn[lastI + 1]  # lastI是需要跟着变的
                    if ltr in temp2:
                        lastI += counter
                maxLen.append(srcIn[firstI:lastI + 1])
                print("firstI" + str(firstI))
                print("lastI" + str(lastI))
                print(maxLen)
            return 0


if __name__ == "__main__":
    testInput = input()
    s = solution()
    s.hwTest(testInput)
    while True:
        try:
            testInput = input()
            s = solution()
            s.hwTest(testInput)
        except IndexError:
            break
