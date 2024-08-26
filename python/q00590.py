"""
590. N-ary Tree Postorder Traversal

Given the `root` of an n-ary tree, return the postorder traversal of its nodes'
values.

Nary-Tree input serialization is represented in their level order traversal.
Each group of children is separated by the null value (See examples)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """O(log_N n) time, O(n) space solution"""
        if not root:
            return []

        result = []
        for child in root.children:
            result += self.postorder(child)
        
        result += [root.val]

        return result
        
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        return [node for child in root.children for node in self.postorder(child)] + [root.val]