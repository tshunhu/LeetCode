#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        peak = float('-inf')
        res = 0
        for i, top in enumerate(A):
            if top > peak:
                peak=top
                res = i

        return res 
        
        '''
        # 二分查找速度更快
        low = 0
        high = len(A) - 1
        while low <= high:
            mid = (low + high) // 2
            if   A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid - 1] < A[mid] and A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        '''


# @lc code=end

