# Program
Leetcode Practice
It is a practice about Algorithm achieved by Python
Dynamic programming could be divided into 2 parts(1.Optimiztion i.e. Maxium value(10,5,70,30,50) 2.Count Line dp[i][j] = dp[i-1][j] + dp[i][j-1])
1.dynamic programming (ClimbStairs/Fib/tribonacci/deleteAndEarn)
   1.1 Pay more attention to 2 crucial array,which means dp[] and sums[]
   1.2 show solicitude for the equation of state transition.    dp[i] = max(dp[i-1],dp[i-2]+sums[i])  The dp[i] correspond to sums[i] in same function
   1.3 focus on the init statement. such as the structure of sums[] and the init value of dp[0,1]
2.matrix dynamic programming(uniquePaths/minPathSum/uniquePathsWithObstacles/minimumTotal/minFallingPathSum/maximalSquare)

