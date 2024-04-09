class Solution:
    @staticmethod
    def hw_test(test_in):
        src_in = test_in
        rep_l = []
        for i in src_in:
            cnt = src_in.count(i)
            if (cnt == 1) and (i not in rep_l):
                rep_lf = src_in.find(i)  # the first index
                rep_ll = src_in.rfind(i)  # the last index
                # keep this sequence...
                rep_l.append(rep_lf)
                rep_l.append(rep_ll)
                rep_l.append(i)
        if len(rep_l) == 0:
            return 1
        else:
            print(rep_l)
            times = int(len(rep_l) * 3)
            first_i = 0
            last_i = 0
            max_len = []
            for i in range(times):
                # first_i = rep_l[3:i]
                # last_i = rep_l[3:i + 1]
                counter = 0
                temp1 = src_in[first_i:last_i]  # 重复字符之间的字符
                for ltr in temp1:
                    counter += 1
                    temp2 = src_in[last_i + 1]  # lastI是需要跟着变的
                    if ltr in temp2:
                        last_i += counter
                max_len.append(src_in[first_i:last_i + 1])
                print("first_i" + str(first_i))
                print("last_i" + str(last_i))
                print(max_len)
            return 0


if __name__ == "__main__":
    testInput = input()
    s = Solution()
    s.hw_test(testInput)
    while True:
        try:
            testInput = input()
            s = Solution()
            s.hw_test(testInput)
        except IndexError:
            break
