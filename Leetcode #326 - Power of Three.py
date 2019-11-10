import math

class Solution:
    def isPowerOfThree(self, n):
        '''
        >>> solution = Solution()
        >>> solution.isPowerOfThree(1)
        True
        >>> solution.isPowerOfThree(2)
        False
        >>> solution.isPowerOfThree(3)
        True
        >>> solution.isPowerOfThree(4)
        False
        >>> solution.isPowerOfThree(9)
        True
        >>> solution.isPowerOfThree(27)
        True
        >>> solution.isPowerOfThree(81)
        True
        '''
        
        if n < 1:
            return False
        
        x = math.log(n,3)
        return abs(x - round(x)) < 0.0000000000001


if __name__ == '__main__':
    import doctest
    doctest.testmod()