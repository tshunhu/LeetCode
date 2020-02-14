#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        '''
        addresses = set()
        for email in emails:
            at = email.find('@')
            name = email[:at].replace('.', '')
            plus = name.find('+')
            if plus != -1:
                name=name[:plus]
            addresses.add(name+email[at:])

        return len(addresses)
        '''
        
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)


# @lc code=end

