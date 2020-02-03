#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True

        counts = 0
        if nums[0]>nums[1]:  #保证第一和第二个元素的顺序。这里性能比在nums前插入一个-Inf快，虽然后者代码量更小更美
            counts+=1
            nums[0]=nums[1]
        
        for i in range(1,n-1):
            '''
            注意：到这一步，从0到i位置的元素已经是正确的顺序
            如果nums[i]>nums[i+1]，说明要调整，【敲黑板】调整的原则是尽量把大数往小里调，为后面排序留空间。
            所以先看看能不能调小i（因为i元素较大），实在不行则调大i+1
            '''
            if nums[i]>nums[i+1]:
                #要调整先+1,达到次数就退出
                counts += 1
                if counts > 1:
                    return False
                
                #调整，先调小i，不行则调大i+1
                if nums[i+1]>=nums[i-1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
                
        return True
        '''
        length = len(nums)
        flag = 0
        pos = 0
        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                if flag == 0:
                    flag = 1
                    pos = i
                else:
                    return False
        if flag == 0:
            return True
        if length == pos + 2 or pos == 0:
            return True
        if nums[pos-1] <= nums[pos+1] or nums[pos] <= nums[pos+2]:
            return True
        return False
        '''
# @lc code=end

