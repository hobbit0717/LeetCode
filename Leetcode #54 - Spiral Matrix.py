class Solution:
    def spiralOrder(self, matrix):
        '''
        >>> solution = Solution()
        >>> solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        >>> solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        '''
        result = []
        # store and remove the first row of matrix and rotate the matrix
        # counter clockwise and repeat until matrix is empty
        while matrix:
            first_row = matrix.pop(0)
            for elem in first_row:
                result.append(elem)
            matrix = self.helper(matrix)
        return result
    # helper function that rotates matrix counter clockwise
    def helper(self, matrix):
        return list(map(list, zip(*matrix)))[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()