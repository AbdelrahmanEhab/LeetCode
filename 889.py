from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        st = []
        root = TreeNode(preorder[0])
        st.append(root)
        i, j = 1, 0

        while st:
            if st[-1].val == postorder[j]:
                j += 1
                st.pop()
                continue

            node = TreeNode(preorder[i])
            
            if not st[-1].left: st[-1].left = node
            else: st[-1].right = node
            
            i += 1
            st.append(node)

        return root
    
        # Time Complexity : o(n)
        # Space Complexity : o(n)
