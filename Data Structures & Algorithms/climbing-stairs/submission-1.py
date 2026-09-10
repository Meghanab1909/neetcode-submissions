class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0] * n
        dp[0] = 1 #Base Case 1: if no.of steps = 1
        dp[1] = 2 #Base Case 2: if no.of 
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]