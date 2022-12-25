

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findDuplicateSubtrees(self, root):
        visited_notes_hash_map = {}
        answer_map = {}
        self.preorderTraversal(root, visited_notes_hash_map, answer_map)
        answer = list(answer_map)

        if len(answer_map) > 2:
            answer = answer[:-1]
        print(answer)

        return answer

    def preorderTraversal(self, root, visited_map, answer_map):
        if root is None:
            return

        if root.left is None:
            left_value = None
        else:
            left_value = root.left.val

        if root.right is None:
            right_value = None
        else:
            right_value = root.right.val

        if visited_map.__contains__(root.val) and visited_map[root.val] == [left_value, right_value]:
            answer_map[root] = [left_value, right_value]
        else:
            visited_map[root.val] = [left_value, right_value]

        self.preorderTraversal(root.left, visited_map, answer_map)

        self.preorderTraversal(root.right, visited_map, answer_map)

        return


a = TreeNode(val=0, left=TreeNode(val=0, left=TreeNode(val=0, left=None, right=None), right=None), right=TreeNode(
    val=0, left=None, right=TreeNode(val=0, left=None, right=TreeNode(val=0, left=None, right=None))))


# a = TreeNode(val=2, left=TreeNode(val=1, left=None, right=None),
#              right=TreeNode(val=1, left=None, right=None))

# TreeNode(val=0,left=None,right=None)

sol = Solution()
sol.findDuplicateSubtrees(a)
