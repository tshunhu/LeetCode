#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '' : return 0

        l_needle = len(needle)
        for i in range(len(haystack)-l_needle+1):
            if haystack[i:i+l_needle] == needle:
                return i
        
        return -1
# @lc code=end

