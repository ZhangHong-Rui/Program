class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        maxVal = max(nums)
        total = [0] * (maxVal + 1)
        for val in nums:
            total[val] += val

        def rob(nums: List[int]) -> int:
            size = len(nums)
            dp = [nums[0], max(nums[0], nums[1])]
            for i in range(2, size):
                dp.append(max(dp[i-2]+nums[i],dp[i-1]))
            return dp[-1]
        return rob(total)
