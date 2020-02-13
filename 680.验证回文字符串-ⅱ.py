#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                # 舍弃左边字符
                right = s[l+1:r+1]
                # 舍弃右边字符
                left = s[l:r]
                return left == left[::-1] or right == right[::-1]
            l, r = l+1, r-1
        return True


# @lc code=end

