#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            total = max(total + num, num)
            max_sum = max(total, max_sum)
            
        return max_sum        
# @lc code=end

