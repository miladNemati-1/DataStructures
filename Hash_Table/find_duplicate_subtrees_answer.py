class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root):

        res = []

        hmap = {}

        def recurse(node, path):
            if node is None:
                return '#'

            path += ','.join([str(node.val), recurse(node.left,
                             path), recurse(node.right, path)])

            if path in hmap:
                hmap[path] += 1
                if hmap[path] == 2:
                    res.append(node)
            else:
                hmap[path] = 1

            return path

        recurse(root, '')
        print(hmap)
        print(res)
        return res


a = TreeNode(val=0, left=TreeNode(val=0, left=TreeNode(val=0, left=None, right=None), right=None), right=TreeNode(
    val=0, left=None, right=TreeNode(val=0, left=None, right=TreeNode(val=0, left=None, right=None))))


# a = TreeNode(val=2, left=TreeNode(val=1, left=None, right=None),
#              right=TreeNode(val=1, left=None, right=None))

# TreeNode(val=0,left=None,right=None)

sol = Solution()
sol.findDuplicateSubtrees(a)
