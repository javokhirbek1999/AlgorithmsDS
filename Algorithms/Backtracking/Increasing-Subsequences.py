class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        
        res = []
        
        self.backtrack(nums, 0, [], res)
        
        return res
    
    
    def backtrack(self, nums: List[int], index: int, subseq: List[int], res: List[List[int]]):
        
        if len(subseq) > 1:
            res.append(subseq[:])
        
        
        added = {}
        
        for i in range(index, len(nums)):
                            
            if len(subseq) > 0 and subseq[-1] > nums[i]: 
                continue
            
            if nums[i] in added:
                continue
                
            added[nums[i]] = 1
            
            subseq.append(nums[i])
            
            self.backtrack(nums, i+1, subseq, res)

            subseq.pop()
