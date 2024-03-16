# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxi = float('-inf')
    def calculateInfectionTime(self, root: Optional[TreeNode], start: int, is_start_node: bool) -> int:
        if not root:return 0
        if root.val == start and is_start_node:
            self.maxi = max(self.maxi, self.calculateInfectionTime(root, start, False) - 1)
            return -1
        left_height = self.calculateInfectionTime(root.left, start, is_start_node);right_height = self.calculateInfectionTime(root.right, start, is_start_node)
        if left_height < 0 or right_height < 0:
            self.maxi = max(self.maxi, abs(left_height) + abs(right_height));return min(left_height, right_height) - 1
        return max(left_height, right_height) + 1
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.calculateInfectionTime(root, start, True)
        return self.maxi
        