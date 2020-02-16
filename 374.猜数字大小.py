#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        '''
        l = 1
        r = n

        while l<=n:
            mid = (l+r)//2
            res = guess(mid)
            if res == -1:
                r = mid-1
            elif res == 1:
                l = mid+1
            else:
                return mid
        '''
        
        # 三分查找
        l = 1
        r = n

        while l <= n:
            mid1 = l + (r-l)//3
            mid2 = r - (r-l)//3
            res1, res2 = guess(mid1), guess(mid2)

            if res1 == 0:
                return mid1
            if res2 == 0:
                return mid2

            if res1 == -1:
                r = mid1 - 1
            elif res2 == 1:
                l = mid2 + 1
            else:
                l, r = mid1 + 1, mid2 - 1


# @lc code=end
