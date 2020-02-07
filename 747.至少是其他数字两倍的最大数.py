#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1 : return 0

        pos_fist = 0
        first = float('-inf')
        second = float('-inf')
        for i, num in enumerate(nums):
            if num > first:
                pos_fist = i
                second = first
                first = num
            elif num > second:
                second = num
        
        if second == 0 or  first / second >= 2:
            return pos_fist
        
        return -1


# @lc code=end

