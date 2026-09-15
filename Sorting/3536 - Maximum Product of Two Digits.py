'''You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

 

Example 1:

Input: n = 31

Output: 3

Explanation:

The digits of n are [3, 1].
The possible products of any two digits are: 3 * 1 = 3.
The maximum product is 3.'''



from typing import List
class Solution:
    def maxProduct(self, n: int) -> int:
        n=str(n)
        l=[]
        for i in n:
            l.append(int(i))
        l.sort()
        return l[-1]*l[-2]

Solution = Solution()
n = int(input("Enter a positive integer: "))
print(Solution.maxProduct(n))