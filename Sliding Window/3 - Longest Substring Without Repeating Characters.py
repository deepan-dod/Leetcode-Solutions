'''Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.'''



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        l=0
        c=0
        for i in range(len(s)):
            while s[i] in d:
                d.remove(s[l])
                l+=1
            d.add(s[i])
            c=max(c,i-l+1)
        return c