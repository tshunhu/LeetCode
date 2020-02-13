#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#

# @lc code=start
class Solution:
    import math
    def repeatedStringMatch(self, A: str, B: str) -> int:
        '''
        if len(set(A))<len(set(B)):
            return -1

        time=len(B)/len(A)+2

        for i in range(int(time)-2,int(time)):
            if B in A*i:
                return i

        for i in range(0,int(time)):
            tmp_A=A+i*A
            if B in tmp_A:
                return i+1
        
        return -1
        '''
        
        if len(set(A))<len(set(B)):
            return -1

        min_times = max(1, math.ceil(len(B)/len(A)))
        max_times = max(min_times, math.ceil(len(B)/len(A)+2))
        for i in range(min_times, max_times):
            if B in A*i:
                return i
        return -1
        

# @lc code=end

