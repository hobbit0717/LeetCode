# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        '''
        >>> solution = Solution()
        >>> solution.maximumAverageSubtree(Node1)
        13.5
        >>> solution.maximumAverageSubtree(Node11)
        20.0
        '''
        if root.val == None:
            return root
        self.maxAverage = float('-inf')
        self.maxNode = None
        def helper(node):
            if not node: return 0, 0.0
            leftTotal, leftSum = helper(node.left)
            rightTotal, rightSum = helper(node.right)
            
            currentTotal = 1 + leftTotal + rightTotal
            currentSum = node.val + leftSum + rightSum
            
            currentAverage = (currentSum) / (currentTotal)
            if currentAverage > self.maxAverage:
                self.maxAverage = currentAverage
                self.maxNode = node
            return currentTotal, currentSum
        helper(root)
        return self.maxAverage


# example tree from https://en.wikipedia.org/wiki/Binary_search_tree
# -----------------------------------------------------------------------------------------------------
Node1 = TreeNode(8)
Node2 = TreeNode(3)
Node3 = TreeNode(10)
Node4 = TreeNode(1)
Node5 = TreeNode(6)
Node6 = TreeNode(4)
Node7 = TreeNode(7)
Node8 = TreeNode(14)
Node9 = TreeNode(13)

Node1.left = Node2
Node1.right = Node3

Node2.left = Node4
Node2.right = Node5
Node5.left = Node6
Node5.right = Node7

Node3.right = Node8
Node8.left = Node9

# -----------------------------------------------------------------------------------------------------
# modified tree from above
Node11 = TreeNode(8)
Node22 = TreeNode(3)
Node33 = TreeNode(10)
Node44 = TreeNode(1)
Node55 = TreeNode(6)
Node66 = TreeNode(4)
Node77 = TreeNode(7)
Node88 = TreeNode(14)
Node99 = TreeNode(20)

Node11.left = Node22
Node11.right = Node33

Node22.left = Node44
Node22.right = Node55
Node55.left = Node66
Node55.right = Node77

Node33.right = Node88
Node88.left = Node99


if __name__ == '__main__':
    import doctest
    doctest.testmod()