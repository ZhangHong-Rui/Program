class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0,0]
        for i in range(n-1):
            dp.append(min(dp[-1]+cost[i+1],dp[-2]+cost[i]))
        return dp[-1]
