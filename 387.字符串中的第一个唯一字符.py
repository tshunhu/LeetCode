#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1

        '''
        for item in Counter(s).items():
            if item[1] == 1:
                return s.index(item[0])
        return -1
        '''
# @lc code=end

