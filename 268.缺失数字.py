#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        full_total = (1+n)*n//2
        curr_total = sum(nums)
        return full_total - curr_total
        
"""
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

"""
# @lc code=end

