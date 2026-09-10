# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []

        def traverse(root):
            if root:
                traverse(root.left)
                inorder.append(root.val)
                traverse(root.right)
        
        traverse(root)
        
        #Checking for duplicates
        if len(inorder) != len(list(set(inorder))):
            return False
        else:
            return inorder == sorted(inorder)