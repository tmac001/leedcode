# @Time : 2020-03-22 21:51
"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
"""


# 1、罗马数字对应的阿拉伯数字使用字典对应
# 2、对每一个数字进行处理，如果符合特殊情况，可以看成负数
# 3、考虑列表越界，最后对最后一个数字单独相加
def romanToInt(s) -> int:
    luoba = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    num = 0
    lists = list(s)

    for i in range(len(s) - 1):

        if luoba.get(lists[i]) < luoba.get(lists[i + 1]):
            num -= luoba.get(lists[i])
        else:
            num += luoba.get(lists[i])
    last_num = s[len(s) - 1]
    num = num + luoba[last_num]
    return num


print(romanToInt("IM"))
