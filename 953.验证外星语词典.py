#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(1, len(words)):
            for first, second in zip(words[i-1], words[i]):
                if first != second:
                    if order.index(first) > order.index(second):
                        return False
                    break
            else:
                if len(words[i-1]) > len(words[i]):
                    return False

        return True

# @lc code=end
