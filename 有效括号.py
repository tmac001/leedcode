# @Time : 2020-03-26 15:47
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 使用python 列表入栈出栈，append,pop实现
def isValid(s: str) -> bool:
    sict_str = {
        "(": ")",
        "[": "]",
        "{": "}",
        "?": "?"
    }
    if len(s) % 2 != 0: return False
    list_str = ['?']
    for i in s:
        if i in sict_str.keys():
            list_str.append(i)
        else:
            if i != sict_str[list_str.pop()]:
                return False
    return len(list_str) == 1


print(isValid("()"))
