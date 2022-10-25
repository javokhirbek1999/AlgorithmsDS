class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
                
        n = len(nums)
        
        prefix = 0
        
        count = [1] + [0] * k
        
        
        res = 0
        
        for num in nums:
            prefix = (prefix + num) % k
            res += count[prefix]
            count[prefix] += 1
        
        return res
            
