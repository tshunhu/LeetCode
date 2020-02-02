#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        _map = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D': 500, 'CM':800, 'M':1000}
        return sum(_map.get(s[max(i-1, 0):i+1], _map[n]) for i, n in enumerate(s))

        '''
        这题题解中的 _map 就是一个字典，其中 get(key, default) 函数可以通过 key 从 _map 中找出对应的值，
        如果 key 不存在则返回默认值 default
        '''

# @lc code=end

