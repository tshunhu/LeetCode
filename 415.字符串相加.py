#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1)-1, len(num2)-1
        carry = 0
        res = ''
        while l1 >=0 or l2 >=0:
            n1 = int(num1[l1]) if l1 >= 0 else 0
            n2 = int(num2[l2]) if l2 >= 0 else 0
            res = str((n1 + n2 + carry)%10) + res
            carry = (n1 + n2 + carry)//10
            l1-=1
            l2-=1

        return '1' + res if carry else res

# @lc code=end

