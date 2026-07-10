'''You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The final answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1'''



class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n)]
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=1
        for i in range(1,n):
            for j in range(amount+1):
                k=dp[i-1][j]
                t=0
                if j>=coins[i]:
                    t=dp[i][j-coins[i]]
                dp[i][j]=k+t
        return dp[n-1][amount]