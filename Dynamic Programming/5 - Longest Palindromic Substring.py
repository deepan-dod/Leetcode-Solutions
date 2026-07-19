'''Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.'''



class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        a=""
        for i in range(n):
            dp[i][i]=True
            a=s[i]
        m=1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i]==s[j]:
                    if j-i==1 or dp[i+1][j-1]:
                        dp[i][j]=True
                        if m<j-i+1:
                            m=j-i+1
                            a=s[i:j+1]
        return a