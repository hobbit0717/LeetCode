class Solution:
    def isValid(self, s):
        '''
        >>> solution = Solution()
        >>> solution.isValid("()")
        True
        >>> solution.isValid("()[]{}")
        True
        >>> solution.isValid("(]")
        False
        >>> solution.isValid("([)]")
        False
        >>> solution.isValid("{[]}")
        True
        '''
        
        stack = []
        my_dict = {"]":"[", "}":"{", ")":"("}
        
        for char in s:
            if char in my_dict.values():
                stack.append(char)
            elif char in my_dict.keys():
                if stack == [] or my_dict[char] != stack.pop():
                    return False
            else:
                return False
        
        return stack == []


if __name__ == '__main__':
    import doctest
    doctest.testmod()