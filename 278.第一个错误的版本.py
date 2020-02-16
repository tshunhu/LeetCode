#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        last = n
        while first < last:
            mid = (first + last)//2
            if not isBadVersion(mid):
                first = mid+1
            else:
                last = mid
            
        return first 



# @lc code=end

