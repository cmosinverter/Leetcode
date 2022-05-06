# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = [(root, 1)]
        dis = []
        while q:
            u, res = q.pop(0)
            dis.append(res)
            if u.left:
                q.append((u.left, res+1))
            if u.right:
                q.append((u.right, res+1))
        return max(dis)
#Runtime: 48 ms, faster than 71.27% of Python3 online submissions for Maximum Depth of Binary Tree.
#Memory Usage: 15.4 MB, less than 81.37% of Python3 online submissions for Maximum Depth of Binary Tree.
