from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.visited = set()
        
        def dfs(root, val):
            if not root: return
            self.visited.add(val)
            if root.left: dfs(root.left, val*2+1)
            if root.right: dfs(root.right, val*2+2)
            return
    
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.visited


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)