'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false'''



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=list(s)
        l1=list(t)
        if sorted(l)==sorted(l1):
            return True
        else:
            return False