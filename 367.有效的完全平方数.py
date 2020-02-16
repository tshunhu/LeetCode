#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        l = 1
        r = num//2

        while l <= r:
            mid = (l + r )//2
            if mid*mid < num:
                l = mid+1
            elif mid*mid > num:
                r = mid-1
            else:
                return True

        return False
            

        

# @lc code=end
