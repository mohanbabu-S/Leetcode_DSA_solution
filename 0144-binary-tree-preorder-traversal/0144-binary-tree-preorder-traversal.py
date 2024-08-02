# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        while stack:
            currentNode = stack.pop()
            if currentNode:
                res.append(currentNode.val)
                stack.append(currentNode.right)
                stack.append(currentNode.left)
        return res