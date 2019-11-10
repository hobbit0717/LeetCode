class Solution(object):
    # easy
    def isStrobogrammatic(self, num):
        '''
        >>> solution = Solution()
        >>> solution.isStrobogrammatic('69')
        True
        >>> solution.isStrobogrammatic('88')
        True
        >>> solution.isStrobogrammatic('962')
        False
        >>> solution.isStrobogrammatic('9681896')
        True
        '''
        dic = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        res = []
        for d in list(num):
            if d in dic:
                res.append(dic[d])
            else:
                return False
        return list(num) == res[::-1]
    
    
    # hard
    def isStrobogrammatic2(self, num):
        '''
        >>> solution2 = Solution()
        >>> solution2.isStrobogrammatic2('69')
        True
        >>> solution2.isStrobogrammatic2('88')
        True
        >>> solution2.isStrobogrammatic2('962')
        False
        >>> solution2.isStrobogrammatic2('9681896')
        True
        '''
        # below is original but not as efficient as edited ver
        #return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)//2+1))
        
        # edited ver
        for i in range(len(num)//2 + 1):
            if num[i] + num[~i] not in '696 00 11 88':
                return False
        return True
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()