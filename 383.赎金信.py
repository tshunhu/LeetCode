#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h_map = defaultdict(int)
        for char in magazine:
            h_map[char] += 1

        for char in ransomNote:
            h_map[char] -= 1    
            if h_map[char] < 0:
                return False
                
        return True
        
# @lc code=end

