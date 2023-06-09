    def climbStairs(self, n: int) -> int:
        s=[1,2]
        if n<=2:
            return s[n-1]
        while len(s)<n:
            s.append(s[-1]+s[-2])
        return s[-1]

     
# remember recursion
memo = [-1] * (n - 1)
def climbStairs(self, n: int) -> int:
    def dfs(i: int, memo) -> int:
        if i == 0 or i == 1:
            return 1
        if memo[i] == -1:
            memo[i] = dfs(i - 1, memo) + dfs(i - 2, memo)
        return memo[i]
    return dfs(n, memo)
