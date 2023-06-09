    def rob(self, nums: List[int]) -> int:
        dp = [nums[0],max(nums[0],nums[1])]    
        if len(nums) <= 2:
            return dp[len(nums)-1]
        i = 2
        while len(dp) < len(nums) and i < len(nums):
            dp.append(max(dp[-1],dp[-2]+nums[i])) 
            i+=1
        return dp[-1]
        

   def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur

