   def fib(self, n: int) -> int:
        dp = [0,1]
        if n <= 1: return dp[n]
        while len(dp) <= n:
            dp.append(dp[-2]+dp[-1])
        return dp[-1]
        
   def tribonacci(self, n: int) -> int:
        dp = [0,1,1]
        if n <= 2:
            return dp[n]
        while len(dp)<= n:
            dp.append(dp[-3]+dp[-2]+dp[-1])
        return dp[-1]
