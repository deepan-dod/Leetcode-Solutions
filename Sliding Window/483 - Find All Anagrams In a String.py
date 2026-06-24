'''Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".'''



class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        l=[0]*26
        l1=[0]*26
        res=[]
        for i in range(len(p)):
            l[ord(p[i])-97]+=1
        for i in range(len(p)):
            l1[ord(s[i])-97]+=1
        if l==l1:
            res.append(0)
        i,j=1,len(p)
        while j<len(s):
            l1[ord(s[i-1])-97]-=1
            l1[ord(s[j])-97]+=1
            if l==l1:
                res.append(i)
            i+=1
            j+=1
        return res