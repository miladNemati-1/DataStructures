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



        self.preorderTraversalPrinting(root.left, answer)
        answer.append(root.val)
        print(root.val)

        self.preorderTraversalPrinting(root.right, answer)

        return

    def preorderTraversal(self, root):
        result = []
        self.preorderTraversalPrinting(root, result)
        print(result)

        return result


a = TreeNode(val= 8, left= TreeNode(val= 2,left=None, right=None), right= TreeNode(val= 7,left=None, right=None))
sol = Solution()
sol.preorderTraversal(a)


