"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""


def twoSum1(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for n in range(i + 1, len(nums)):
            if (nums[i] + nums[n]) == target:
                return [i, n]


# 考虑暴力循环时间复杂度，改进逻辑
def twoSum2(nums: list, target: int) -> list:
    for i in range(len(nums)):
        num = target - nums[i]
        if num in nums[:i]:
            if i == nums.index(num):
                continue
            return [i, nums.index(num)]


# 使用集合的方式，存贮下标和元素，省去判断是否在列表中的开销
def twoSum3(nums: list, target: int) -> list:
    dict_nums = {}
    for i, n in enumerate(nums):
        dict_nums[n] = i
    for i, num in enumerate(nums):
        j = dict_nums.get(target - num)
        if j != i and j is not None:
            return [i, j]


a = [1, 2, 8]
print(twoSum1(a, 10))
