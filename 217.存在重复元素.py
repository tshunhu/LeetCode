#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
"""
        _map = {}
        for i in nums:
            if _map.get(i) != None:
                return True
            _map[i] = 0
        return False
"""
# @lc code=end

