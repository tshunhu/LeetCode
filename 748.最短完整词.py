#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短完整词
#

# @lc code=start
import collections
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate = filter(lambda ch: ch.isalpha(), licensePlate.lower())
   
        lics_count = collections.Counter(plate)
        
        words = sorted(words, key=lambda x: len(x))

        for word in words:
            if collections.Counter(word)&lics_count==  lics_count:
                return word



        
# @lc code=end

