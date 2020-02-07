#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # left 记录一个元素最左边的位置, right记录最右边的位置, count记录出现的频率
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans

# @lc code=end

