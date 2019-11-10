class Solution:
    # my version
    def flipAndInvertImage(self, A):
        '''
        >>> solution = Solution()
        >>> solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
        [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
        '''
        for row in A:
            row.reverse()
            for i, n in enumerate(row):
                if n == 0:
                    row[i] = 1
                elif n == 1:
                    row[i] = 0
        
        return A

    # advanced version
    def flipAndInvertImage2(self, A):
        '''
        >>> solution = Solution()
        >>> solution.flipAndInvertImage2([[1,1,0],[1,0,1],[0,0,0]])
        [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
        '''    

        return [[1-i for i in row[::-1]] for row in A]
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()