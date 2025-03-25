#Link: https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = []
        q.append(root)
        ans = []
        while q:
            size = len(q)
            res = []
            for _ in range(size):
                node = q.pop(0)
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(res[-1])
        return ans