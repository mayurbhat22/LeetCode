#Link: https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root):
            if not root:
                return 0
            left_tree_height = traverse(root.left)
            right_tree_height = traverse(root.right)

            if left_tree_height == -100000 or right_tree_height == -100000:
                return -100000

            if abs(left_tree_height - right_tree_height) > 1:
                return -100000
            else:
                return max(left_tree_height, right_tree_height) + 1
        
        val = traverse(root)
        return False if val == -100000 else True
