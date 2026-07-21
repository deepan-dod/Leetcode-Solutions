'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2'''



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        p=0
        f={0:1}
        for i in nums:
            p+=i
            if p-k in f:
                c+=f[p-k]
            if p not in f:
                f[p]=1
            else:
                f[p]+=1
        return c