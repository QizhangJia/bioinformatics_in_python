# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not preorder:
            return None

        root = preorder[0]

        p = 0
        while inorder[p] != root:
            p += 1
        # pointer p stops at root.

        left = self.buildTree(preorder[1:p+1], inorder[:p])
        right = self.buildTree(preorder[p+1:], inorder[p+1:])

        return TreeNode(root, left, right)
