class MinStack:
    '''
    >>> my_stack = MinStack()
    >>> my_stack.push(5)        # [5]
    >>> my_stack.push(3)        # [5, 3]
    >>> my_stack.push(1)        # [5, 3, 1]
    >>> my_stack.pop()          # [5, 3]
    >>> my_stack.top()          # return 3
    3
    >>> my_stack.push(9)        # [5, 3, 9]
    >>> my_stack.push(2)        # [5, 3, 9, 2]
    >>> my_stack.push(5)        # [5, 3, 9, 2, 5]
    >>> my_stack.push(6)        # [5, 3, 9, 2, 5, 6]
    >>> my_stack.getMin()       # return 2
    2
    '''

    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.stack == []:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()