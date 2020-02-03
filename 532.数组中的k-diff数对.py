#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的K-diff数对
#

# @lc code=start


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0        

        saw, diff = set(), set()
        # 看见一对中任意一个数, 就将大的存起来
        for num in nums:
            if num+k in saw:
                diff.add(num+k)
            if num-k in saw:
                diff.add(num)
            saw.add(num)

        return len(diff)
# @lc code=end
