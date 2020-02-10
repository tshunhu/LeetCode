#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
import functools
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        
        x, y, z = 0, 1, 1
        for _ in range(n - 2):
            x, y, z = y, z, x + y + z
        return z

    '''
    # 思路2：递归，加上lru缓存，就不用重复计算啦，加速加速
    @functools.lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n==0:return 0
        if n==1:return 1
        if n==2:return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
    '''
# @lc code=end

