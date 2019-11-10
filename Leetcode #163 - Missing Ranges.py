class Solution:
    def findMissingRanges(self, nums, lower, upper):
        '''
        >>> solution = Solution()
        >>> solution.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
        ['2', '4->49', '51->74', '76->99']
        '''
        nums = [lower-1] + nums + [upper+1]
        ranges = []

        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 2:
                ranges.append(str(nums[i] + 1))
            elif nums[i+1] - nums[i] > 2:
                ranges.append(str(nums[i] + 1) + '->' + str(nums[i+1] - 1))

        return ranges


if __name__ == '__main__':
    import doctest
    doctest.testmod()