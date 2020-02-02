#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1 : 
            return '1'

        s = self.countAndSay(n-1)

        count = 1
        prev = s[0]
        res = ''
        
        for i in range(1, len(s)):
            if prev == s[i]: 
                count+=1
            else:
                res = ''.join([res, str(count), prev])
                count = 1
                prev = s[i]

        res = ''.join([res, str(count), s[-1]])
        
        return res        
# @lc code=end

