#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)

        accu = 0

        for i in A:
            accu += i
            if accu == total // 3:
                accu = 0
        
        return accu == 0
# @lc code=end

