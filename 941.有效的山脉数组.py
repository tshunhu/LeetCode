#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        length = len(A)

        if length < 3:
            return False

        i = 0

        # 上行
        while i+1 < length and A[i] < A[i+1]:
            i += 1

        # 顶点不能是两端
        if i == 0 or i == length - 1:
            return False

        #下行
        while i+1 < length and A[i] > A[i+1]:
            i += 1

        # 顺利走完则返回True
        return i == length - 1

# @lc code=end
