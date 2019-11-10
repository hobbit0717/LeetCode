class Solution:
    def merge(self, intervals):
        '''
        >>> solution = Solution()
        >>> solution.merge([[1, 4], [4, 5]])
        [[1, 5]]
        >>> solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        [[1, 6], [8, 10], [15, 18]]
        >>> solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        [[1, 6], [8, 10], [15, 18]]
        >>> solution.merge([[5, 5], [1, 2], [2, 4], [2, 3], [4, 4], [5, 5], [2, 3], [5, 6], [0, 0], [5, 6]])
        [[0, 0], [1, 4], [5, 6]]
        
        '''
        out = []
        for i in sorted(intervals):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out += i,
        return out
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()