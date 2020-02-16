#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''
        return int((math.sqrt(1+8*n)-1)/2)
        '''

        l = 0
        r = n // 2 + 1
        while l < r:
            # 加1是为什么?
            mid = (l + r + 1) // 2
            total = mid * (mid+1) / 2
            if total < n:
                l = mid
            elif total > n:
                r = mid - 1
            else:
                return mid
        return l

# @lc code=end
