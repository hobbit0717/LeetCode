class Solution:
    def getHint(self, secret, guess):
        '''
        >>> solution = Solution()
        >>> solution.getHint('1807', '7810')
        '1A3B'
        >>> solution.getHint('1123', '0111')
        '1A1B'
        >>> solution.getHint('11', '11')
        '2A0B'
        >>> solution.getHint('10001', '01110')
        '0A4B'
        '''
        bull, cow = 0, 0
        s = {} # secret hashtable
        g = {} # guess hashtable
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1

        for k in s:
            if k in g:
                cow += min(s[k], g[k])
        
        return '{0}A{1}B'.format(bull, cow)


if __name__ == '__main__':
    import doctest
    doctest.testmod()