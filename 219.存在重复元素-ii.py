#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        _map = {}

        for i, num in enumerate(nums):
            if num not in _map:
                _map[num] = i
            else:
                if i - _map[num] <= k:
                    return True
                else:
                    _map[num] = i
        
        return False
# @lc code=end

