def canPartition(nums: List[int]) -> bool:
        
        _sum = sum(nums)
        
        if _sum % 2 == 1:
            return False
        
        target = _sum//2
        
        dp = {}
        
        return solve(nums, 0, target, dp)
    
  def solve(nums, index, target, dp):

      if target == 0:
          return True

      if index == len(nums) or target < 0:
          return False

      key = (index, target)

      if key in dp:
          return dp[key]

      if nums[index] > target:
          dp[key] = solve(nums, index+1, target, dp)
      else:
          dp[key] = solve(nums, index+1, target-nums[index], dp) or self.solve(nums, index+1, target, dp)

      return dp[key]
