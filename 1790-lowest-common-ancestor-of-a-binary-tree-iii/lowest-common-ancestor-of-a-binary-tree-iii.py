"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        # 2 equally sized but different paths, p+q = q+p, find their first intersection

        a_node = p
        b_node = q

        while a_node != b_node:
            if a_node.parent:
                a_node = a_node.parent
            else: 
                a_node = q
            if b_node.parent:
                b_node = b_node.parent
            else:
                b_node = p
        
        return a_node