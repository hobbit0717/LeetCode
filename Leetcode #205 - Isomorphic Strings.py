class Solution:
    def isIsomorphic(self, s, t):
        '''
        >>> solution = Solution()
        >>> solution.isIsomorphic('egg', 'add')
        True
        >>> solution.isIsomorphic('foo', 'bar')
        False
        >>> solution.isIsomorphic('paper', 'title')
        True
        >>> solution.isIsomorphic('ab', 'aa')
        False
        >>> solution.isIsomorphic('abc', 'ddf')
        False
        '''
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()