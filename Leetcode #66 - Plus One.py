class Solution:
    # Ver 1 - convert list to int, add 1, convert back to list
    def plusOne(self, digits):
        '''
        >>> solution = Solution()
        >>> solution.plusOne([1, 2, 3, 4])
        [1, 2, 3, 5]
        >>> solution.plusOne([5, 1, 2, 7])
        [5, 1, 2, 8]
        >>> solution.plusOne([9, 9, 9, 9])
        [1, 0, 0, 0, 0]
        >>> solution.plusOne([3, 5, 7, 9])
        [3, 5, 8, 0]
        >>> solution.plusOne([0])
        [1]
        >>> solution.plusOne([9])
        [1, 0]
        '''
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        return [int(i) for i in str(num + 1)]
    
    # Ver 2 - addition from the last elem of list
    def plusOne2(self, digits):
        '''
        >>> solution = Solution()
        >>> solution.plusOne2([1, 2, 3, 4])
        [1, 2, 3, 5]
        >>> solution.plusOne2([5, 1, 2, 7])
        [5, 1, 2, 8]
        >>> solution.plusOne2([9, 9, 9, 9])
        [1, 0, 0, 0, 0]
        >>> solution.plusOne2([3, 5, 7, 9])
        [3, 5, 8, 0]
        >>> solution.plusOne2([0])
        [1]
        >>> solution.plusOne2([9])
        [1, 0]
        
        '''
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)        
        
        
    # Ver 3 - recursion
    def plusOne3(self, digits):
        '''
        >>> solution = Solution()
        >>> solution.plusOne3([1, 2, 3, 4])
        [1, 2, 3, 5]
        >>> solution.plusOne3([5, 1, 2, 7])
        [5, 1, 2, 8]
        >>> solution.plusOne3([9, 9, 9, 9])
        [1, 0, 0, 0, 0]
        >>> solution.plusOne3([3, 5, 7, 9])
        [3, 5, 8, 0]
        >>> solution.plusOne3([0])
        [1]
        >>> solution.plusOne3([9])
        [1, 0]
        '''
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]

        elif digits[-1] != 9:
            digits[-1] += 1
            return digits

        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne3(digits[:-1])
            return digits

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()