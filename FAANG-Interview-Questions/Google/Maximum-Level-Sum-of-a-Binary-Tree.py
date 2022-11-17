"""

n = # of levels
m = # of nodes in each level

Time: O(n * m)
Space: O(m)

"""
from collections import deque 


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        
        queue.append(root)
        
        
        maxLevelSum = -math.inf
        maxLevel = 0
        currentLevel = 1
        
        while queue:
            currentLevelSum = 0
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                
                currentLevelSum += node.val
                
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if maxLevelSum < currentLevelSum:
                maxLevelSum = currentLevelSum
                maxLevel = currentLevel
            
            currentLevel += 1
        
        return maxLevel
                
