import operator

class Solution:
    # Straightforward Version
    def islandPerimeter(self, grid):
        '''
        >>> solution = Solution()
        >>> solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
        16
        '''
        grid_x = ['0' + ''.join(str(each_cell) for each_cell in row) + '0' for row in grid]
        grid_y = ['0' + ''.join(str(each_cell) for each_cell in col) + '0' for col in zip(*grid)]
        return sum([row.count('01') + row.count('10') for row in grid_x + grid_y])
    
    # Advanced Version
    def islandPerimeter2(self, grid):
        '''
        >>> solution = Solution()
        >>> solution.islandPerimeter2([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
        16
        '''
        return sum(sum(map(operator.ne, [0] + row, row + [0]))
                   for row in grid + list(map(list, zip(*grid))))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    