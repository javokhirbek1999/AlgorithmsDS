"""
n = # of emais
m = # of characters

Time: O(n * m)
Space: O(n)
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        uniqueEmails = set()
        
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            uniqueEmails.add(local+'@'+domain)
        
        return len(uniqueEmails)
