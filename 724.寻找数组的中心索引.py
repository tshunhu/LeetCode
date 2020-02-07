#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        acc = 0
        for i, num in enumerate(nums):
            if acc == (total-num) / 2:
                return i
            acc+=num
        return -1




# @lc code=end

