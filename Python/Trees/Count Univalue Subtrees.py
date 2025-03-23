#Link: https://leetcode.com/problems/count-univalue-subtrees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0

        def traverse(root):
            nonlocal count
            if not root:
                return -2000
            left_tree = traverse(root.left)
            right_tree = traverse(root.right)

            if left_tree == -2000 or right_tree == -2000:
                if (left_tree == -2000 and right_tree == -2000) or (left_tree == -2000 and right_tree == root.val) or (right_tree == -2000 and left_tree == root.val):
                    count += 1
                    return root.val
            elif left_tree == right_tree == root.val:
                count += 1
                return root.val
            else:
                return -1500
            
        traverse(root)
        return count