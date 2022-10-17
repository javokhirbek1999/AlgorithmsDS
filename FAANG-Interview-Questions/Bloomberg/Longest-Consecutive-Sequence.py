class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        
        nums = sorted(set(nums))
        
        c = 1
        
        mx = 1

        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                c += 1
            else:
                mx = max(mx, c)
                c = 1
        
        mx = max(mx, c)
        
        return mx
        
