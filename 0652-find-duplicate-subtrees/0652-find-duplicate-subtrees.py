# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        
        def solve(r):
            if not r:
                return "#"
            
            s = ""
            if not r.left and not r.right:
                s += str(r.val)
                hashmap[s] = hashmap.get(s, 0) + 1
                if hashmap[s] == 2:
                    duplicates.append(r) 
                return s
            
            s += str(r.val)+","+solve(r.left)+","+solve(r.right) 
            hashmap[s] = hashmap.get(s, 0) + 1
            if hashmap[s] == 2:
                duplicates.append(r) 
            return s
        
        hashmap = {}
        duplicates = [] 
        solve(root) 
        return duplicates 