#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(nums)*len(nums[0]) or r == len(nums)  : return nums

        row = []
        res = []
        col = 0
        for rows in nums:
            for num in rows:
                row.append(num)
                col+=1
                if col % c == 0:
                    res.append(row)
                    row = []

        return res
# @lc code=end

