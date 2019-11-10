class Solution:
    # official solution
    def addStrings(self, num1, num2):
        ''' (str, str) -> str
        >>> solution = Solution()
        >>> solution.addStrings('1', '2')
        '3'
        >>> solution.addStrings('999', '999')
        '1998'
        >>> solution.addStrings('0', '439')
        '439'
        
        '''
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = ord(num1.pop())-ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop())-ord('0') if len(num2) > 0 else 0
            
            temp = n1 + n2 + carry 
            res.append(temp % 10)
            carry = temp // 10
        if carry: res.append(carry)
        return ''.join([str(i) for i in res])[::-1]
    
    # my version
    def addStrings2(self, num1, num2):
        ''' (str, str) -> str
        >>> solution = Solution()
        >>> solution.addStrings2('1', '2')
        '3'
        >>> solution.addStrings2('999', '999')
        '1998'
        >>> solution.addStrings2('0', '439')
        '439'
        '''
        actual_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                      '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}
        
        first_num = second_num = 0
        
        for each_char in num1:
            first_num = first_num * 10 + actual_num[each_char]
        
        for each_char2 in num2:
            second_num = second_num * 10 + actual_num[each_char2]
            
        return str(first_num + second_num)        


if __name__ == '__main__':
    import doctest
    doctest.testmod()