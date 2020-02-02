#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    # 双指针
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
        return i+1

    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        map = {}
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i]+=1
        
        for k ,v in map.items():
            for i in range(v-1):
                nums.remove(k)
            
        return len(nums)
    '''
# @lc code=end

