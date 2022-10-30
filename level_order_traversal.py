# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if root is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(root.left)
        rheight = height(root.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


class Solution:



    def levelOrderAddToQueue(self, root):
        if root is None:
            return []
        order = []
        queue = []
        queue.append(root)

        while (len(queue) > 0):
            order.append([queue[0].val])
            root = queue.pop(0)




            if not root.left is None:
                queue.append(root.left)

            if not root.right is None:
                queue.append(root.right)

        return order






binary_tree = TreeNode(0, TreeNode(2, TreeNode(1, TreeNode(5), TreeNode(1))), TreeNode(4, TreeNode(3, TreeNode(6)), TreeNode(-1, None, TreeNode(8))))
sol = Solution()

print(sol.levelOrderAddToQueue(binary_tree))

