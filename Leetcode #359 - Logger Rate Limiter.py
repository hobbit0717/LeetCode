# the key point is to keep memery small.
# if stored msg is away 10 sec from timestamp,
# remove the msg whenever it gets a new message.
# Note that in Python 3.6 and beyond, dictionaries
# are ordered data structures.

class Logger:
    def __init__(self):
        self.msgStored = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        >>> solution = Logger()
        >>> solution.shouldPrintMessage(1, "foo")
        True
        >>> solution.shouldPrintMessage(1, "poo")
        True
        >>> solution.shouldPrintMessage(2, "bar")
        True
        >>> solution.shouldPrintMessage(3, "foo")
        False
        >>> solution.shouldPrintMessage(8, "bar")
        False
        >>> solution.shouldPrintMessage(10, "foo")
        False
        >>> solution.shouldPrintMessage(11, "foo")
        True
        >>> solution.shouldPrintMessage(13, "bar")
        True
        >>> solution.shouldPrintMessage(22, "bar")
        False
        >>> solution.shouldPrintMessage(23, "bar")
        True
        """
        # if each stored message is 10 secs away
        # from the timestamp, remove it
        # if the difference is bigger than 10 secs, break
        for old_message in self.msgStored.copy():
            if self.msgStored[old_message] + 10 <= timestamp:
                self.msgStored.pop(old_message)
            else:
                break
            
        if message not in self.msgStored:
            self.msgStored[message] = timestamp
            return True
        
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()