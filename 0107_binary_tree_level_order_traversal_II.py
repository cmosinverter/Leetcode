# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([(root, 0)])
        table = defaultdict(list)
        while q:
            u , dis = q.popleft()
            table[dis].append(u.val)
            if u.left:
                q.append((u.left, dis+1))
            if u.right:
                q.append((u.right, dis+1))
        return list(table.values())[::-1]
#Runtime: 38 ms, faster than 78.08% of Python3 online submissions for Binary Tree Level Order Traversal II.
#Memory Usage: 14.2 MB, less than 48.54% of Python3 online submissions for Binary Tree Level Order Traversal II.
