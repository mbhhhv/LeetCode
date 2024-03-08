class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        a = 0
        for num in nums:
            b = 0
            if num - 1 not in nums:
                while num in nums:
                    num = num + 1
                    b = b + 1
            a = max(a,b)
        return a



s = Solution()
s.longestConsecutive([4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3])
