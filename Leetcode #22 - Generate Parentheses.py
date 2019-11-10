class Solution:
    # backtracking 1 (able to understand)
    def generateParenthesis(self, n):
        '''
        >>> solution = Solution()
        >>> solution.generateParenthesis(3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']
        '''

        if n == 0:
            return []
        def generate(curr, num_available, num_unclosed):
            if num_available == 0:
                return [curr + ')' * num_unclosed]
            elif num_unclosed == 0:
                return generate(curr + '(', num_available - 1, num_unclosed + 1)
            return generate(curr + '(', num_available - 1, num_unclosed + 1) + \
                   generate(curr + ')', num_available, num_unclosed - 1)
        return generate('', n, 0)
    
    # backtracking 2 (from here on, unable to understand)
    def generateParenthesis2(self, n):
        '''
        >>> solution = Solution()
        >>> solution.generateParenthesis2(3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']
        '''        
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)    


    # backtracking 3 (result is different order... need more analysis)
    def generateParenthesis3(self, n, open=0):
        '''
        >>> solution = Solution()
        >>> solution.generateParenthesis3(3)
        ['()()()', '()(())', '(())()', '(()())', '((()))']
        '''        
        if n == 0: return [')'*open]
        if open == 0:
            return ['('+x for x in self.generateParenthesis3(n-1, 1)]
        else:
            return [')'+x for x in self.generateParenthesis3(n, open-1)] + ['('+x for x in self.generateParenthesis3(n-1, open+1)]


    # backtracking 4
    def generateParenthesis4(self, n, open=0):
        '''
        >>> solution = Solution()
        >>> solution.generateParenthesis4(3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']
        '''             
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis4(n-1, open+1)] + \
                   [')' + p for p in self.generateParenthesis4(n, open-1)]
        return [')' * open] * (not n)    


    # without recursion (result is different order... need more analysis)
    def generateParenthesis5(self, n):
        '''
        >>> solution = Solution()
        >>> solution.generateParenthesis5(3)
        ['()()()', '()(())', '(())()', '(()())', '((()))']
        '''             
        res = []
        s = [("(", 1, 0)]
        while s:
            x, l, r = s.pop()
            if l - r < 0 or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(x)
            s.append((x+"(", l+1, r))
            s.append((x+")", l, r+1))
        return res
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()