import re


class Solution:
    """
    https://javaziliao.com/post/4065.html
    华为OD机试 - 模拟数据序列化传输
    题目描述
    模拟一套简化的序列化传输方式，请实现下面的数据编码与解码过程:
    编码前数据格式为 [位置,类型,值]，多个数据的时候用逗号分隔，
    位置仅支持数字，不考虑重复等场景；
    类型仅支持：Integer / String / Compose（Compose的数据类型表示该存储的数据也需要编码）

    编码后数据参考图示，数据区的格式是：位置#类型#长度#数据，
    类型存储需要编码，Integer->0；String->1；Compose->2，
    长度是指数据的字符长度；
    数据仅允许数字、大小写字母、空格。
    输入的编码字符长度不能超过1000，一个数据的格式错误，则解析剩下数据，其他错误输出ENCODE_ERROR。
    输入的解码字符不能超过1000，数据区异常则跳过继续解析剩余数据区，其他异常输出DECODE_ERROR。

    输入描述
    输入有两行：
    第一行是命令，1表示编码，2表示解码
    第二行输入待编码/解码的字符
    数据最多嵌套10层，[1,Compose,[1,String,Second]] 为2层嵌套。
    """
    @staticmethod
    def encode(src):
        stk = []
        tmp = ""
        for ii, chara in enumerate(src, 0):
            if chara == "[" and len(tmp) == 0:
                stk.append("[")
            if re.match(r"[0-9a-zA-Z ]", chara):
                tmp += chara
            if chara == "," and len(tmp) != 0:
                stk.append(tmp)
                tmp = ""
            if chara == "]":  # 遇到"]"则pop，生成的数据也append道stk中。
                # print(["stk to pop:", stk])
                stk.append(tmp)
                tmp = ""
                scur = list()
                spop = ""
                while spop != "[":
                    spop = stk.pop()
                    scur.append(spop)
                # print(["scur:", scur])
                if scur[-1] == "[" and scur[-3] == "Integer":
                    stk.append(scur[-2] + "#0#" + str(len(scur[-4]) + 1) + "#" + scur[-4])
                    # print(["stk after Integer added:", stk])
                if scur[-1] == "[" and scur[-3] == "String":
                    stk.append(scur[-2] + "#1#" + str(len(scur[-4]) + 1) + "#" + scur[-4])
                    # print(["stk after String added:", stk])
                if scur[-1] == "[" and scur[-3] == "Compose":
                    data = ""
                    for css in scur[-4::-1]:
                        data = data + css
                    stk.append(scur[-2] + "#2#" + str(len(data) + 1) + "#" + data)
                    # print(["stk after Compose added:", stk])
        print(["Final stk:", stk])
        return "".join(stk)


if __name__ == "__main__":
    ss1 = '[1,String,I am hell0],[2,Integer,23],[3,Long,10000]'
    ss2 = '[1,String,I am hell0],[2,Integer,23],[3,Long,10000],[4,Compose,[1,String,testtest]]'
    ss3 = '[1,String,I am hell0],[2,Integer,23],[3,Long,10000],[4,Compose,[1,String,testtest],[2,Integer,222222]]'
    ss4 = ('[1,String,I am hell0],[2,Integer,23],[3,Long,10000],[4,Compose,[1,String,testtest],'
           '[2,Compose,[1,Integer,66666]],[3,String,testtest]]')
    slt = Solution()
    print(slt.encode(ss4))
