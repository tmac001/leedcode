# @Time : 2020-03-25 15:19
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
"""


# 当列表没有元素是，返回”“
# 当列表有一个元素时，全部匹配，返回这个元素
# 当列表大于一个元素时，开始对比：整体思路：取出列表第一个字符串后，拿该字符串的元素与后面列表元素字符串相同索引值对比，
# 1、第一层循环：取出列表中第一个元素的，每个字符
# 2、 第二层循环：取出列表第一个元素后的所有元素，与第一个元素的每个字符串比较
# 3、当
def longestCommonPrefix(strs) -> str:
    if len(strs) == 0:
        return ''
    elif len(strs) == 1:
        return strs[0]
    else:
        for i in range(len(strs[0])):
            c = strs[0][i]
            for n in range(1, len(strs)):
                if i == len(strs[n]) or c != strs[n][i]:
                    return strs[0][:i]
        return strs[0]


print(longestCommonPrefix(["ll", "l"]))
