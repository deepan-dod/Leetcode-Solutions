'''Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]'''



from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        j=len(s)-1
        i=0
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1

Solution = Solution()
s = list(input("Enter the string characters separated by commas: ").split(","))
Solution.reverseString(s)
print("Reversed string:", s)