'''An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.'''



class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[0]*n
        a=b=c=0
        dp[0]=1
        for i in range(1,n):
            dp[i]=min(dp[a]*2,dp[b]*3,dp[c]*5)
            if dp[i]==dp[a]*2:
                a+=1
            if dp[i]==dp[b]*3:
                b+=1
            if dp[i]==dp[c]*5:
                c+=1
        return dp[n-1]