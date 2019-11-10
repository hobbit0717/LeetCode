import bisect


#min(w) will give smallest character for each word 'w' in 'words' list
#w.count(min(w)) will give frequency of smallest character for each word 'w' in 'words' list
#'f' is the sorted frequency list of 'words'
#For each query 'q' in 'queries' list, we find its rightmost suitable index in the frequency 'f' list
#Total length of frequency list 'f' minus index will give answer[i]
#Index is determined by bisect module, which gives number of words having frequency of their smallest character less than or equal to query 'q'

class Solution:
    def numSmallerByFrequency(self, queries, words):
        '''
        >>> solution = Solution()
        >>> solution.numSmallerByFrequency(["cbd"], ["zaaaz"])
        [1]
        >>> solution.numSmallerByFrequency(["bbb","cc"], ["a","aa","aaa","aaaa"])
        [1, 2]
        '''
        f = sorted(w.count(min(w)) for w in words)
        return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]

if __name__ == '__main__':
    import doctest
    doctest.testmod()