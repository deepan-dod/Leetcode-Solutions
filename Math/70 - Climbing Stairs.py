'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps'''


'Method 1'
class Solution:
    def climbStairs(self, n: int) -> int:
        ans=0
        for i in range(n):
            ans+=comb(n-i,i)
        return ans


'Method 2'
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,1
        for i in range(1,n+1):
            a,b=b,a+b
        return a