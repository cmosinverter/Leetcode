# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack1, sums = [root], defaultdict(list)
        sums[root].append(root.val)
        res = []
        while stack1:
            u = stack1.pop()
            if u.left:
                stack1.append(u.left)
                sums[u.left].append(u.left.val)
                sums[u.left] += sums[u]
                
            if u.right:
                stack1.append(u.right)
                sums[u.right].append(u.right.val)
                sums[u.right] += sums[u]
            if not u.left and not u.right and sum(sums[u]) == targetSum:
                a = sums[u]
                a.reverse()
                res.append(a)
        return res
#Runtime: 59 ms, faster than 54.36% of Python3 online submissions for Path Sum II.
#Memory Usage: 19.5 MB, less than 9.71% of Python3 online submissions for Path Sum II.
