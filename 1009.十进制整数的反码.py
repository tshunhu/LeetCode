#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        '''
        N+反码的值的二进制应该为'11...1'长度就是N的二进制数的长度n，
        其和值就是 1+2^1+...+2^(n-1) = 2^n-1 , 直接带入计算即可
        '''

        return 2**(len(bin(N))-2)-1-N
        
# @lc code=end

