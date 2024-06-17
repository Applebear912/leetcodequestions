# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sum = 0

    def inOrder(self, node, low, high):
        if not node:
            return
        if node.val >= low and node.val <= high:
            self.sum += node.val
        self.inOrder(node.left, low, high)
        self.inOrder(node.right, low, high)

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.inOrder(root, low, high)
        return self.sum

            
    