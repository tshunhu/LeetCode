#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = {}
        for i, num in enumerate(nums):
            if _map.get(target - num) is not None:
                return [i, _map.get(target - num)]
            _map[num] = i
        
# @lc code=end

