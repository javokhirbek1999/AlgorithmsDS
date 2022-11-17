"""
Time: O(n log n)
Space: O(n)
"""

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        
        for i in range(len(arrive)):
            
            arrive[i] = (arrive[i], 'A')
            depart[i] = (depart[i], 'D')
        
        comb = sorted(arrive + depart)
        
        for x in comb:
            
            if x[1] == 'A':
                if K == 0:
                    return False
                K -= 1
            else:
                K += 1
        
        return True
