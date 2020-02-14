#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 重复 N 次的元素
#

# @lc code=start
import collections
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        '''
        for k in range(1, 4):
            for i in range(len(A)-k):
                if A[i] == A[i+k]:
                    return A[i]
        '''
        A.sort()
        for i in range(len(A) - 1):
            if A[i] == A[i + 1]:
                return A[i]
# @lc code=end

