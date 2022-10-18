"""

n = # of nodes
h = tree height

Time: O(n)
Space: O(h)
"""
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        paths = []
        
        self.paths(root, [], 0, paths)
        
        return paths
    
    def paths(self, root, path, pathLen, paths):
        
        if not root:
            return path
        
        
        if pathLen < len(path):
            path[pathLen] = root.val
        else:
            path.append(root.val)
            pathLen += 1
        
        
        if self.isLeafNode(root):
            paths.append("->".join(str(val) for val in path))
        
        self.paths(root.left, path, pathLen, paths)
        self.paths(root.right, path, pathLen, paths)
        
        path.pop()
    
    def isLeafNode(self, root):
        return root and not root.left and not root.right
        
        
