# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.subtree_set = collections.defaultdict(int)
        self.ans = []
        if root:
            self.dfs(root)
        return self.ans
    
        
    def dfs(self, root):
        if root.left is None and root.right is None:
            # this is a leaf node
            tree_str = "(#)" + str(root.val) + "(#)"
            self.subtree_set[tree_str] += 1
            if self.subtree_set[tree_str] == 2:
                # only returns one of the duplicated subtrees
                self.ans.append(root)
            return tree_str
                
        left_ts = "#"
        if root.left:
            left_ts = self.dfs(root.left)
        
        left_ts = "(" + left_ts + ")" + str(root.val)
        right_ts = "#"
        if root.right:
            right_ts = self.dfs(root.right)
            
        tree_str = left_ts + "(" + right_ts + ")"
        self.subtree_set[tree_str] += 1
        if self.subtree_set[tree_str] == 2:
            self.ans.append(root)
        return tree_str
        