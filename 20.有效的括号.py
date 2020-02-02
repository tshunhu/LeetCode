#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        _map = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in _map:
                top_element = stack.pop() if stack else '#'
                if top_element != _map[char] :      
                    return False
            else:
                stack.append(char)
        return not stack
        
# @lc code=end

