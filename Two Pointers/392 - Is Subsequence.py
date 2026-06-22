'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true'''



class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0 and len(t)==0 or len(s)==0:
            return True
        if len(t)==0:
            return False
        i,j=0,0
        while j<len(t):
            if i<len(s) and s[i]==t[j]:
                i+=1
            j+=1
        if i==len(s):
            return True
        return False  