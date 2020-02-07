#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

# @lc code=start
import collections
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        for domain in cpdomains:
            # 分开访问次数 和 域名
            count, domain = domain.split()
            count = int(count)
            # 分割域名
            frags = domain.split('.')
            # 组合域名中的字段, 从整体开始, 然后不断排除前面的
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count

        return [f'{ct} {dom}' for dom, ct in ans.items()]


# @lc code=end

