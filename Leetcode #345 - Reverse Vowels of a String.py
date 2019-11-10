class Solution:
    def reverseVowels(self, s):
        '''
        >>> solution = Solution()
        >>> solution.reverseVowels('hello')
        'holle'
        >>> solution.reverseVowels('leetcode')
        'leotcede'
        '''
        vowel = 'AEIOUaeiou'
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while (s[i] not in vowel) and (i < j):
                i += 1
            while (s[j] not in vowel) and (i < j):
                j -= 1
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
            
        return ''.join(s)
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()