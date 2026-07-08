class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        l = len(coins)
        dp = [[float('inf')]*(amount+1) for _ in range(l)]
        if amount==0:
            return 0
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i] = i//coins[0]
        for i in range(1,l):
            for j in range(amount+1):
                if j==0:
                    dp[i][j]=float('inf')
                elif j-coins[i]<0:    
                    dp[i][j] = dp[i-1][j]
                elif j-coins[i]==0:
                    dp[i][j]=1
                elif j-coins[i]>0:
                    if dp[i][j-coins[i]]:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-coins[i]]+1)
                    else:
                        dp[i][j] = float('inf')
        
        
        if dp[l-1][amount]!=float('inf'):
            return dp[l-1][amount]
        else:
            return -1
