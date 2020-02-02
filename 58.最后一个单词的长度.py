#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        count = 0
        flag = False
        
        for c in s[::-1]:
            if c != ' ':
                count += 1
                flag = True
            else:
                if flag:
                    return count
        return count
'''
        if not s:
            return 0
        
        s_list = s.split(" ")
        s_list.reverse()

        for i in s_list:
            if len(i) != 0 :
                return len(i)
        return 0    
'''    
# @lc code=end

