#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #我们将出现过的数字对应的数组下标上的元素值始终变为负数，那么数组中正数的元素的下标可以表示缺失的元素。

        for num in nums:
            nums[abs(num)-1] = abs(nums[abs(num)-1])*-1

        res = []
        for i, num in enumerate(nums):
            if num > 0: 
                res.append(i+1)
        
        return res
# @lc code=end

