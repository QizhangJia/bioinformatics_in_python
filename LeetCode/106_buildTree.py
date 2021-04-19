# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        if not inorder:
            return None

        root = postorder[-1]

        p = 0
        while p < len(inorder) and inorder[p] != root:
            p += 1
        # pointer p stops at root of inorder.

        left = self.buildTree(inorder[:p], postorder[:p])
        right = self.buildTree(inorder[p+1:], postorder[p:-1])

        return TreeNode(root, left, right)
