#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        '''
        我们可以对 bits\mathrm{bits}bits 数组从左到右扫描来判断最后一位是否为一比特字符。
        当扫描到第 iii 位时，如果 bits[i]=1\mathrm{bits}[i]=1bits[i]=1，那么说明这是一个两比特字符，
        将 iii 的值增加 2。如果 bits[i]=0\mathrm{bits}[i]=0bits[i]=0，那么说明这是一个一比特字符，将 iii 的值增加 1。
        如果 iii 最终落在了 bits.length−1\mathrm{bits}.\mathrm{length}-1bits.length−1 的位置，
        那么说明最后一位一定是一比特字符。
        '''
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1

        '''
        事實上因為只要數組最後一個數是0，那麼這個數組肯定可以被0，10，11分割。
        那麼只需要考慮最後一個0前面連續1的個數，個數是偶數則TRUE，否則FALSE。所以從數組末尾開始遍歷效率會更高。
        '''
        '''
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0

        '''

        

# @lc code=end

