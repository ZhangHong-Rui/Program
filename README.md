# Program
Leetcode Practice
It is a practice about Algorithm achieved by Python
1.dynamic programming (ClimbStairs/Fib/tribonacci/deleteAndEarn)
   1.1 Pay more attention to 2 crucial array,which means dp[] and sums[]
   1.2 show solicitude for the equation of state transition.    dp[i] = max(dp[i-1],dp[i-2]+sums[i])  The dp[i] correspond to sums[i] in same function
   1.3 focus on the init statement. such as the structure of sums[] and the init value of dp[0,1]
