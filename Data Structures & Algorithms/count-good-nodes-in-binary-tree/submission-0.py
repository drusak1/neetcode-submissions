# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        amount_good_nodes = 0
        def dfs(node,max_el):
            nonlocal amount_good_nodes

            if node is None:
                return
            if node.val >= max_el:
                max_el = node.val
                amount_good_nodes += 1
            dfs(node.left, max_el)
            dfs(node.right, max_el)
        dfs(root, float("-inf"))
        return amount_good_nodes
