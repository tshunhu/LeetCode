#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        res = sum(nums[:k])
        tmp = res
        for i in range(k, len(nums)):
            tmp = tmp - nums[i-k]+nums[i]
            if res < tmp :
                res = tmp
            

        return res/k
# @lc code=end

