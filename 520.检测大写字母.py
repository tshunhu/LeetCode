#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()):
            return True
        else:
            return False
        '''

        first_upper = word[0].isupper()

        # 0 默认, 1 全大写, 2 首字母大写
        all_up_flag = 0

        for char in word[1:]:
            # 首字母非大写, 后续有大写
            if not first_upper and char.isupper():
                return False

            # 首字母大写, 后续遇到小写
            if first_upper and char.islower() and all_up_flag == 0:
                all_up_flag = 2

            # 首字母大写, 后续遇到大写
            if first_upper and char.isupper() and all_up_flag == 0:
                all_up_flag = 1


            if first_upper and all_up_flag == 2 and char.isupper():
                return False

            if first_upper and all_up_flag == 1 and char.islower():
                return False


        return True
        '''
# @lc code=end

