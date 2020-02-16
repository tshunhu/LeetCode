#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        l, r = 0, len(s)-1

        cpyStr = list(s)

        while l<r:
            if cpyStr[l] not in vowels:
                l+=1
            if cpyStr[r] not in vowels:
                r-=1
            if cpyStr[l] in vowels and cpyStr[r] in vowels:
                cpyStr[l], cpyStr[r] = cpyStr[r], cpyStr[l]
                l, r = l+1, r-1

        return ''.join(cpyStr)
# @lc code=end

