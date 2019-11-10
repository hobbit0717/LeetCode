class Solution:
    def findDisappearedNumbers(self, nums):
        '''
        >>> solution = Solution()
        >>> solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])
        [5, 6]
        '''
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
    
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
    
    
    def findDisappearedNumbers2(self, nums):
        '''
        >>> solution = Solution()
        >>> solution.findDisappearedNumbers2([4,3,2,7,8,2,3,1])
        [5, 6]
        '''    
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
                    
        return [i + 1 for i, num in enumerate(nums) if num > 0]    


    def findDisappearedNumbers3(self, nums):
        '''
        >>> solution = Solution()
        >>> solution.findDisappearedNumbers3([4,3,2,7,8,2,3,1])
        [5, 6]
        '''
        return list(set(range(1, len(nums)+1)).difference(set(nums)))
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

