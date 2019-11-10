class Solution:
    def numUniqueEmails(self, emails):
        '''
        >>> solution = Solution()
        >>> solution.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
        2
        '''
        unique_email = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            unique_email.add(local + '@' + domain)

        return len(unique_email)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()