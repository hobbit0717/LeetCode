class Solution:
    def searchRange(self, nums, target):
        '''
        >>> solution = Solution()
        >>> solution.searchRange([5,7,7,8,8,10], 8)
        [3, 4]
        >>> solution.searchRange([5,7,7,8,8,10], 6)
        [-1, -1]
        '''
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target + 1) - 1] if target in nums[lo:lo+1] else [-1, -1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()