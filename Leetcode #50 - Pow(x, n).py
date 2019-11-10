class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        >>> solution = Solution()
        >>> solution.myPow(2.0, 10)
        1024.0
        >>> solution.myPow(2.1, 3)
        9.261000000000001
        >>> solution.myPow(2.0, -2)
        0.25
        '''
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)

        return self.myPow(x*x, n/2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()