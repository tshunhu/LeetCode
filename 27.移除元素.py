#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #  双指针
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            while left < right and nums[left] != val:
                left += 1
            while left < right and nums[right] == val:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        for i in range(n):
            if nums[i] == val:
                return i

'''
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0 : return 0
        
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
                j+=1
            else:
                j+=1

        return i
'''
# @lc code=end
