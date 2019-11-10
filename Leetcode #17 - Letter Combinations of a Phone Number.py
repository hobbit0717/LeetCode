class Solution:
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    
    # Ver1 - recursion using above
    def letterCombinations(self, digits):
        ''' (str) -> List[str]
        >>> solution = Solution()
        >>> solution.letterCombinations('')
        []
        >>> solution.letterCombinations('23')
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        '''
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(self.mapping[digits])
        
        all_combs = self.letterCombinations(digits[:-1])
        new_comb = self.mapping[digits[-1]]
        return [each_comb + each_chr for each_comb in all_combs for each_chr in new_comb] 


    # Ver2 - for loop
    def letterCombinations2(self, digits):
        ''' (str) -> List[str]
        >>> solution = Solution()
        >>> solution.letterCombinations2('')
        []
        >>> solution.letterCombinations2('23')
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        '''        
        nums_to_letters = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                           '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        combs = [''] if digits else []
        
        for digit in digits:
            new_combs = []
            for comb in combs:
                for letter in nums_to_letters[digit]:
                    new_combs.append(comb + letter)
            combs = new_combs
            
        return combs


if __name__ == '__main__':
    import doctest
    doctest.testmod()