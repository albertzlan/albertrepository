# 通过逗号分割输入字符串
tmp2 = "1,33<C>,2<A>00".split(",")
# 创建一个字典来存储每个单元格的内容
cells = {chr(65 + i): tmp2[i] for i in range(len(tmp2))}
# 遍历每个单元格
result = ""
for cell in tmp2:
    # 找到"<"和">"的位置
    result1 = cell.find("<")
    result2 = cell.find(">")
    # 如果单元格不包含"<"和">"，将其添加到结果字符串中
    if result1 == -1 and result2 == -1:
        result += cell + ","
    # 如果单元格包含"<"或">"，但格式不正确，打印-1并退出程序
    elif result1 == -1 or result2 == -1 or result1 > result2 or result2 - result1 != 2:
        print(-1)
        exit(0)
    # 如果单元格包含正确的引用，将引用替换为实际的单元格值，并将处理后的单元格添加到结果字符串中
    else:
        result += cell[:result1] + cells[cell[result1 + 1]] + cell[result2 + 1:] + ","
# 打印处理后的结果字符串，删除末尾的逗号
print(result[:-1])
