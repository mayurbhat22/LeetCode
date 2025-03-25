#Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def traverse(node, max_val):
            if not node:
                return 0
            left_tree_count = traverse(node.left, max(max_val, node.val))
            right_tree_count = traverse(node.right, max(max_val, node.val))

            if node.val >= max_val:
                return left_tree_count + right_tree_count + 1
            else:
                return left_tree_count + right_tree_count

        return traverse(root, float("-inf"))
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def traverse(node, max_val):
            nonlocal count
            if not node:
                return
            traverse(node.left, max(max_val, node.val))
            traverse(node.right, max(max_val, node.val))

            if node.val >= max_val:
                count += 1
            return 

        traverse(root, float("-inf"))
        return count