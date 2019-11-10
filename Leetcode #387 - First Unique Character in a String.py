class Solution:
    def firstUniqChar(self, s):
        '''
        >>> solution = Solution()
        >>> solution.firstUniqChar("leetcode")
        0
        >>> solution.firstUniqChar("loveleetcode")
        2
        '''
        basket = {}
        seen = set()
        
        for its_index, each_char in enumerate(s):
            if each_char not in seen:
                basket[each_char] = its_index
                seen.add(each_char)
            elif each_char in basket:
                del basket[each_char]

        if basket:
            return min(basket.values())
        
        return -1
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()