import re


def jiexi(src):
    print("-------------jiexi:")
    regint = r"(\[[0-9]{1,},Integer,[0-9A-Za-z ]{1,}\],{0,1}){1}"
    regstr = r"(\[[0-9]{1,},String,[0-9A-Za-z ]{1,}\],{0,1}){1}"
    # regcomp = r"\[[0-9]{1,},Compose,((\[[0-9]{1,},[StringInteger]{1,},[0-9A-Za-z ]{1,}\],{0,1}){1,})\]"
    # 很难合理匹配Compose嵌套的结尾
    regcomp = r"\[[0-9]{1,},Compose,([0-9A-Za-z, \[\]]{1,}$)"
    regz = r"\[[0-9A-Za-z, ]{1,}\],{0,1}"
    res_list = list()
    while len(src) > 0:
        print(["jiexi src:", src])
        # Integer
        res = re.match(regint, src)
        if res:
            print(["regint", res.group()])
            src = src[len(res.group()):]
            res_list.append(res.group())
            continue
        # String
        res = re.match(regstr, src)
        if res:
            print(["regstr", res.group()])
            src = src[len(res.group()):]
            res_list.append(res.group())
            continue
        # Compose
        res = re.match(regcomp, src)
        if res:
            print(["regcomp", res.group()])
            src = src[len(res.group()):]
            res_list.append(res.group())
            continue
        # Error
        res = re.match(regz, src)
        if res:
            print(["regz dropped...", res.group()])
            # res_list.append(res.group())
            src = src[len(res.group()):]
    print(["res_list:", res_list])
    print("-------------jiexi DONE")
    return res_list


def encode(src):
    print("---------------------encode:")
    ssrc = jiexi(src)
    dst = ""
    print([ssrc])
    for ss in ssrc:
        if ss[-1] == ",":
            ss = ss[:-1]
        # print(ss)
        ssp = ss.split(",")
        print(ssp)
        if len(ssp) == 3:
            if ssp[1] == "Integer":
                dst += ssp[0][1:] + "#0#" + str(len(ssp[2]) + 1) + "#" + ssp[2][:-1]
            if ssp[1] == "String":
                dst += ssp[0][1:] + "#1#" + str(len(ssp[2]) + 1) + "#" + ssp[2][:-1]
        if ssp[1] == "Compose":
            nxts = ",".join(ssp[2:])
            print(["Handle Compose:", nxts])
            tmp = encode(",".join(ssp[2:]))
            dst += ssp[0] + "#2#" + str(len(tmp) + 1) + "#" + tmp
    print("---------------------encode DONE")
    return dst


class Solution:
    @staticmethod
    def mydo(src):
        print([len(src), src])
        idxcomp = []
        cflag = True
        idxc = -1
        idxz = -1
        while cflag:
            idxc = src.find(",Compose,", idxc + 1)
            if idxc == -1:
                cflag = False
            else:
                idxcomp.append(idxc)
        idxz = src.find("]]", idxz + 1)  # 如果字符串中有此字符就悲剧：只含数字、大小字母。
        print(idxcomp)
        print(src[idxcomp[0]:idxcomp[0] + 9])
        print(src[idxz:idxz + 2])
        # return encode(src)


if __name__ == "__main__":
    s = Solution()
    print(s.mydo(
        '[1,String,I am hell0],[2,Integer,23],[3,Long,10000],[4,Compose,[1,String,testtest],[2,Compose,[1,Integer,'
        '66666]],[3,String,testtest]],[5,String,55555555]'))
