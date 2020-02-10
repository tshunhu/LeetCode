#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#

# @lc code=start
import collections
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        ans = collections.Counter(A[0])
        for i in range(1, len(A)):
            # 字典相交, 剩下的就是在所有字符串中都存在的字母
            ans &= collections.Counter(A[i])

        return list(ans.elements())


# @lc code=end

