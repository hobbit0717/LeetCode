class Solution:
    # method 1 - Stack
    # Time Complexity O(m + n)
    # Space Complexity O(m + n)
    def backspaceCompare(self, S: str, T: str) -> bool:
        '''
        >>> solution = Solution()
        >>> solution.backspaceCompare('ab#c', 'ad#c')
        True
        >>> solution.backspaceCompare('ab##', 'c#d#')
        True
        >>> solution.backspaceCompare('a##c', '#a#c')
        True
        >>> solution.backspaceCompare('a#c', 'b')
        False
        '''
        s1 = self.stack(S, [])
        s2 = self.stack(T, [])
        return s1 == s2

    def stack(self, s, stack):
        for char in s:
            if char != '#':
                stack.append(char)
            else:
                if not stack:
                    continue
                stack.pop()
        return stack


    # method 2 - Two Pointers
    # Time Complexity O(n)
    # Space Complexity O(1)
    def backspaceCompare2(self, S: str, T: str) -> bool:
        '''
        >>> solution = Solution()
        >>> solution.backspaceCompare2('ab#c', 'ad#c')
        True
        >>> solution.backspaceCompare2('ab##', 'c#d#')
        True
        >>> solution.backspaceCompare2('a##c', '#a#c')
        True
        >>> solution.backspaceCompare2('a#c', 'b')
        False
        '''
        # pointer 1 and pointer 2
        p1 = len(S) - 1
        p2 = len(T) - 1

        # from the end, compare each char of S and T
        # using helper function, getChar()
        # if char does not match, return False right away
        while (p1 >= 0) or (p2 >= 0):
            char_s = char_t = ''
            if (p1 >= 0):
                char_s, p1 = self.getChar(S, p1)
            if (p2 >= 0):
                char_t, p2 = self.getChar(T, p2)
            if (char_s != char_t):
                return False

        return True

    # helper function that returns char from s that
    # completed deletion caused by '#' 
    def getChar(self, s, p):
        char, count = '', 0
        while (p >= 0) and (not char):
            if s[p] == '#':
                count += 1
            elif count == 0:
                char = s[p]
            else:
                count -= 1
            p -= 1
        
        return char, p


if __name__ == '__main__':
    import doctest
    doctest.testmod()