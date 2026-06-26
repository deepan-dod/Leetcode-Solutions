'''Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.'''



class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c=0
        a='aeiou'
        for i in range(k):
            if s[i] in a:
                c+=1
        if c==k:
            return c
        i=1
        j=k
        d=c
        while j<len(s):
            if s[i-1] in a:
                c-=1
            if s[j] in a:
                c+=1
            d=max(c,d)
            if d==k:
                return d
            i+=1
            j+=1
        return d