class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums) - 1):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    j = j + 1
                else:
                    j = j + 1

'''
给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个
整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
示例1：
输入：nums = [2, 7, 11, 15], target = 9
输出：[0, 1]
解释：因为
nums[0] + nums[1] == 9 ，返回[0, 1] 

示例2：
输入：nums = [3, 2, 4], target = 6
输出：[1, 2]

示例3：
输入：nums = [3, 3], target = 6
输出：[0, 1]
'''