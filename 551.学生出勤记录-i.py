#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A')<2 and s.count('LLL')<1
        '''
        if s.count('A') > 1 : return False

        consec_L = 0
        for char in list(s):
            if char == 'L':
                consec_L += 1
                if consec_L > 2:
                    return False
            else:
                consec_L = 0

        return True
        '''
# @lc code=end

