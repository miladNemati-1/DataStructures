# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def preorderTraversalPrinting(self, root, answer):
        if root is None:
            return

        answer.append(root.val)

        self.preorderTraversalPrinting(root.left, answer)

        self.preorderTraversalPrinting(root.right, answer)

        return

    def preorderTraversal(self, root):
        result = []
        self.preorderTraversalPrinting(root, result)
        print(result)

        return result


a = TreeNode(val= 1, left= None, right= TreeNode(val= 2, left= TreeNode(val= 3, left= None, right= None), right= None))


