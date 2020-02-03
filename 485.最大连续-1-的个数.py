#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for num in nums:
            if num == 1:
                count+=1
            else:
                res = max(res, count)
                count = 0

        return max(res, count) 
# @lc code=end

