class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        '''
        >>> solution = Solution()
        >>> solution.licenseKeyFormatting('5F3Z-2e-9-w', 4)
        '5F3Z-2E9W'
        >>> solution.licenseKeyFormatting('2-5g-3-J', 2)
        '2-5G-3J'
        >>> solution.licenseKeyFormatting('r', 1)
        'R'
        '''
        S = S.replace('-', '').upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()