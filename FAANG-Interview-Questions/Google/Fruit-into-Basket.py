"""
Time: O(n)
Space: O(1)
"""
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        windowStart = 0
        
        maxFruits = 0
        
        # Stores 2 elements at most
        basket = defaultdict(int)
        
        for windowEnd in range(len(fruits)):
            
            basket[fruits[windowEnd]] += 1
            
            while len(basket) > 2:
                
                fruitStart = fruits[windowStart]
                
                basket[fruitStart] -= 1
                
                if basket[fruitStart] == 0:
                    basket.pop(fruitStart)
                    
                windowStart += 1
            
            maxFruits = max(maxFruits, windowEnd-windowStart + 1)
        
        return maxFruits
