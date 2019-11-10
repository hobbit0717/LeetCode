class Solution:
    def TwoSum(self, nums, target):
        '''
        >>> sample_input = [2, 7, 11, 15]
        >>> sample_target = 9
        >>> solution = Solution()
        >>> solution.TwoSum(sample_input, sample_target)
        [0, 1]
        '''
        basket = {}
        for i, n in enumerate(nums):
            if target - n in basket:
                return [basket[target - n], i]
            basket[n] = i
            


if __name__ == "__main__":
    import doctest
    doctest.testmod()
