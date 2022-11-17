"""
Time: O(n log n)
Space: O(n)
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = [[[x,y], math.sqrt(pow(x-0,2)+pow(y-0,2))] for x,y in points]
        
        
        distances.sort(key=lambda x:x[1])
        
        
        res = []
        
        
        for i in range(k):
            res.append(distances[i][0])
        
        return res
