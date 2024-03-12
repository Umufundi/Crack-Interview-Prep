# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ret = [[]]
        stack = deque([root, None])
        while stack:
            curr = stack.popleft()
            if curr:
                ret[-1].append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
            else:
                if stack:
                    stack.append(None)
                    ret.append([])
        return ret