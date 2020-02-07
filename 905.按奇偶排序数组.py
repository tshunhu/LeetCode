#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = sorted(filter(lambda i: i % 2 == 1, A))
        even = sorted(filter(lambda i: i % 2 == 0, A))
        return even+odd
# @lc code=end

