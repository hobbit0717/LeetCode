class Solution:
    def numIslands(self, grid):
        '''
        >>> myMatrix = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]
        >>> myMatrix2 = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]
        >>> solution = Solution()
        >>> solution.numIslands(myMatrix)
        1
        >>> solution.numIslands(myMatrix2)
        3
        '''
        if not grid or not grid[0]:
            return 0

        total = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    total += self.dfs(grid, i, j)

        return total


    def dfs(self, grid, i, j):
        if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[i])) or (grid[i][j] == '0'):
            return 0

        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        return 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()