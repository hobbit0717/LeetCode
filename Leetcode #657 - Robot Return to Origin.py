class Solution:
    def judgeCircle(self, moves):
        '''
        >>> solution = Solution()
        >>> solution.judgeCircle("UD")
        True
        >>> solution.judgeCircle("LL")
        False
        >>> solution.judgeCircle("LDRRLRUULR")
        False
        >>> solution.judgeCircle("DRLLDLLRURLURULLLRULLRLULLLDDUDLUUUDLLDLDRLDRURDURRLRDLDRDLDDURDUURLLUUURLDRLUULUUDRDRUDURLLRDRRDLDU")
        False
        '''
        # if equal number of moves (up and down, left and right) were made,
        # then it has returned to the origin
        basket = {'U': 0, 'D': 0, 'L': 0, 'R': 0}

        for each_move in moves:
            basket[each_move] += 1

        return (basket['U'] == basket['D']) and (basket['L'] == basket['R'])


    def judgeCircle2(self, moves):
        '''
        >>> solution = Solution()
        >>> solution.judgeCircle2("UD")
        True
        >>> solution.judgeCircle2("LL")
        False
        >>> solution.judgeCircle2("LDRRLRUULR")
        False
        >>> solution.judgeCircle2("DRLLDLLRURLURULLLRULLRLULLLDDUDLUUUDLLDLDRLDRURDURRLRDLDRDLDDURDUURLLUUURLDRLUULUUDRDRUDURLLRDRRDLDU")
        False
        '''        
        # used imaginary number j, since 'U' must be compared with 'D',
        # and 'L' must be compared with 'R'
        direct = {'U': 1, 'D': -1, 'L': 1j, 'R': -1j}
        return 0 == sum(direct[m] for m in moves)


if __name__ == '__main__':
    import doctest
    doctest.testmod()