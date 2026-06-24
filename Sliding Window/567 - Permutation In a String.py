'''Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").'''



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        l=[0]*26
        for i in range(len(s1)):
            l[ord(s1[i])-97]+=1
        l1=[0]*26
        for i in range(len(s1)):   
            l1[ord(s2[i])-97]+=1
        if l==l1:
            return True
        i,j=1,len(s1)
        while j<len(s2):
            l1[ord(s2[i-1])-97]-=1
            l1[ord(s2[j])-97]+=1
            if l1==l:
                return True
            i+=1
            j+=1
        return False