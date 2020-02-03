#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
import math 
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        
        #建立空矩阵
        x, y = len(M), len(M[0])
        ans = [[0]*y for j in range(x)]

        for i in range(x):
            for j in range(y):
                sum_ = count = 0
                for ni in (i - 1, i, i + 1):
                    for nj in (j - 1, j, j + 1):
                        if (0 <= ni < x and 0 <= nj < y):
                            sum_ += M[ni][nj]
                            count += 1
                ans[i][j] = math.floor(sum_ / count)
        return ans

      
# @lc code=end

