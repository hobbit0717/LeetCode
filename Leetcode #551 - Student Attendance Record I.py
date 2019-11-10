class Solution:
    # efficient but longer way
    def checkRecord(self, s: str) -> bool:
        '''
        >>> solution = Solution()
        >>> solution.checkRecord('PPALLP')
        True
        >>> solution.checkRecord('PPALLL')
        False
        '''
        absent, late = 0, 0

        for each_record in s:
            if each_record == 'A':
                absent += 1
                late = 0
                if absent == 2:
                    return False
            elif each_record == 'L':
                late += 1
                if late == 3:
                    return False
            else:
                late = 0
                
        return True
    
    # less efficient but shorter way
    def checkRecord2(self, s: str) -> bool:
        '''
        >>> solution = Solution()
        >>> solution.checkRecord2('PPALLP')
        True
        >>> solution.checkRecord2('PPALLL')
        False
        '''
        return s.count('A') <= 1 and s.count('LLL') == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()