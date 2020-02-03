#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        minus_first, minus_second = float('inf'), float('inf')
        
        for num in nums:
            if num >first:
                third= second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
            
            if num < minus_first:
                minus_second = minus_first
                minus_first = num
            elif num < minus_second:
                minus_second = num
            
        return max(first*second*third, minus_first*minus_second*first)
        
        '''

        nums = sorted(nums)
        v1 = nums[-1] * nums[-2] * nums[-3]
        v2 = nums[0] * nums[1] * nums[-1]
        return max(v1, v2)

        '''
# @lc code=end

