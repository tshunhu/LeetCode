#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps, pt = 0, 0
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
            pt += 1

        return ps == len(s)

        '''
        b = iter(t)  # 迭代器
    	return all(((i in b) for i in s ))
        '''
        
# @lc code=end
