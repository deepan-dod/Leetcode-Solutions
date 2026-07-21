'''Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]'''



class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c=0
        p=0
        f={0:1}
        for i in nums:
            p+=i
            m=p%k
            if m<0:
                m+=k
            if m in f:
                c+=f[m]
                f[m]+=1
            elif m not in f:
                f[m]=1
        return c